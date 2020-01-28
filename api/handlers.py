from http import HTTPStatus as http
from flask import make_response, jsonify
from flask import current_app as app

from .       import db
from .models import Product
from .helper import validator


@validator("name", "price")
def create_product_handler(content):
    app.logger.info("api.create_product_handler")
   
    name = content["name"]
    price = content["price"]
    new_product = Product(name=name, price=price)
    app.logger.info(f"api.create_product_handler: New Product \n\t {new_product}")

    db.session.add(new_product)
    try:
        db.session.flush()
    except:
        return make_response("the certain record exists", http.INTERNAL_SERVER_ERROR)
    db.session.commit()

    response =  make_response("success", http.CREATED)
    response.headers['Location'] = f"/v1/product/{new_product.id}"
    return response


def get_handler(id):
    app.logger.info("api.get_hander")
    record = db.session.query(Product).filter(Product.id == id).first()
    app.logger.info(f"api.get_hander: Filtered record \n\t {record}")
    if record is None:
        return make_response("Item not found", http.NOT_FOUND)
    else:
        return make_response(jsonify(record.to_dict()), http.OK)


def get_all_products_handler():
    app.logger.info("api.get_all_products")
    records = db.session.query(Product).all()
    app.logger.info(records)
    ret = []
    for prod in records:
        ret.append(prod.to_dict())

    app.logger.info(ret)
    return make_response(jsonify(ret), http.OK)