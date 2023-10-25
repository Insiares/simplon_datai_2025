from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy_utils import create_database, database_exists, drop_database
import pandas as pd

engine = create_engine("sqlite://", echo=True)

if database_exists(engine.url):
    drop_database(engine.url)
    print('Little bobby tables, he dropped it')

create_database(engine.url)
print('Database created? :', database_exists(engine.url))

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer,autoincrement=True, primary_key=True)
    name = Column(String(255))
    price = Column(Float)

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))    

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, autoincrement=True, primary_key=True)
    customerid = Column(Integer, ForeignKey("customer.id"))
    productid = Column(Integer, ForeignKey("product.id"))
    customer = relationship("Customer")
    product = relationship("Product")

Base.metadata.create_all(engine)

customers = [{'name' : 'user_1',
               'email' : 'u1@u.fr'},
               {'name' : 'user_2',
               'email' : 'u2@u.fr'}]

products = [{'name' : 'Produit_1',
               'price' : 100},
            {'name' : 'Produit_2',
               'price' : 200}]

orders = [ {'customerid' : 1,
               'productid' : 1},
               {'customerid' : 2,
               'productid' : 2}]

Session = sessionmaker(bind=engine)
session = Session()

user_object = [Customer(**custom) for custom in customers]
products_object = [Product(**prod) for prod in products]
order_object = [Order(**ord) for ord in orders]

session.add_all(user_object)
session.add_all(products_object)
session.add_all(order_object)
session.commit()

#Query for each table
customer_output = session.query(Customer).all()
for cust in customer_output:
    print('id -', cust.id)
    print('name -', cust.name)
    print('email -', cust.email)

results = session.query(Product).all()
for product in results:
    print('ind -', product.id)
    print('name - ', product.name)
    print('price -', product.price)

order_results = session.query(Order).all()
for ords in order_results:
    print('ind -', ords.id)
    print('customerid - ', ords.customerid)
    print('produtid -', ords.productid)

#join query 

big_query = session.query( Order.id, 
                          Product.name, 
                          Customer.name, 
                          Product.price
                          ).join(Product, 
                                Order.productid == Product.id
                         ).join(Customer, 
                                Order.customerid == Customer.id).all()

df = pd.DataFrame(big_query, columns = ['Commandes', 'Produit', 'Nom client', 'Prix'])
print('\n'+79*'#'+'\n')
print('Jointure')
print(df)

#updating an item
produit_2 = session.get(Product, 2)
produit_2.price = 500
session.commit()

query_update = session.query(Product).all()
for ind, product in enumerate(results):
    print('ind -', product.id)
    print('name - ', product.name)
    print('price -', product.price)

#deleting an entry
session.query(Order).filter(Order.id==2).delete()
session.commit()

order_results = session.query(Order).all()
for ind, ords in enumerate(order_results):
    print('ind -', ords.id)
    print('customerid - ', ords.customerid)
    print('produtid -', ords.productid)

session.close()