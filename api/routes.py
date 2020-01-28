from http import HTTPStatus as http
from flask import (Response, request, make_response, render_template, jsonify)
from flask import current_app as app

from .models import Product
from .handlers import (create_product_handler, get_handler, get_all_products_handler)


@app.errorhandler(404)
def page_not_found(error):
   return make_response("Not found", http.NOT_FOUND)

@app.route('/')
@app.route('/index')
def index():
    return make_response("Hello, World!", http.OK)


@app.route('/healthz', methods=['GET'])
def healthz():
    app.logger.info("api.healthz")
    
    ret = '{"status": "ok"}'
    header = {"Content-Type": "application/json"}

    return make_response(ret, http.OK, header)


@app.route('/v1/product', methods=['POST'])
def create_product():
    app.logger.info("api.create_product")
    
    if request.is_json:
        return create_product_handler(request.json)
    else:
        return make_response("Invalid payload", http.BAD_REQUEST)


@app.route("/v1/product/<string:product_id>", methods=["GET", "PUT"])
def product_getter_setter(product_id):
    app.logger.info("api.product_getter_setter")
    
    if request.method == 'PUT':
        pass
    elif request.method == 'GET':
            return get_handler(product_id)
   
    else:
        return make_response("Method not allower", http.METHOD_NOT_ALLOWED)


@app.route("/v1/products", methods=["GET"])
def get_all_products():
    app.logger.info("api.get_all_products")
    return get_all_products_handler()
