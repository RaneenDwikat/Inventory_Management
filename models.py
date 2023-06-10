from datetime import datetime

from connectDB import db, app

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.String(10), primary_key=True)
    # productMovements = db.relationship('ProductMovement',backref='product', foreign_keys='ProductMovement.productId')
    def __init__(self, product_id):
        self.product_id = product_id

class Location(db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(db.String(10), primary_key=True)
    # from_lo = db.relationship('ProductMovement',backref='from_lo', foreign_keys='ProductMovement.from_location')
    # to_lo = db.relationship('ProductMovement',backref='to_lo', foreign_keys='ProductMovement.to_location')
    def __init__(self,location_id):
        self.location_id=location_id

class ProductMovement(db.Model):
    __tablename__ = 'product_movements'
    movement_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    productId = db.Column(db.String(10))
    qty = db.Column(db.Integer)
    from_location = db.Column(db.String(100),nullable=True)
    to_location = db.Column(db.String(100),nullable=True)
    timestamp= db.Column(db.DateTime,default= datetime.utcnow)

    def __init__(self,productId,qty,from_location,to_location,timestamp):
        self.productId=productId
        self.qty=qty
        self.from_location=from_location
        self.to_location=to_location
        self.timestamp=timestamp
@app.before_request
def create_tables():
    db.create_all()
