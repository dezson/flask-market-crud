from . import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Pruduct {self.name} {self.price}>'

    def to_dict(self):
        # Hiding ID in the json
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name is not "id"}