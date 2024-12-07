from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    name = db.Column(db.String(230), nullable = False)
    email = db.Column(db.String(120), index = True, unique = True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    todo = db.Column(db.String(140), nullable = False)
    description = db.Column(db.Text, nullable = True)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))

class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    nama = db.Column(db.String(230), nullable = False)
    harga = db.Column(db.Integer(255), nullable = False)
    created_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)

class Category_product(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    kategori = db.Column(db.String(230), nullable = False)
    created_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    product_id = db.Column(db.BigInteger, db.ForeignKey(Product.id))

    def __repr__(self):
        return '<user {}>'.format(self.name)