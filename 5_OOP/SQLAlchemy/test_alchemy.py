
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy_utils import create_database, database_exists, drop_database

engine = create_engine("sqlite://", echo=True)

if database_exists(engine.url):
    drop_database(engine.url)
    print('Little bobby tables, he dropped it')

create_database(engine.url)
print('Database created? :', database_exists(engine.url))

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    price = Column(Float)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

produit1 = Product(id=1, name='Produit_1', price=100)
produit2 = Product(id=2, name='Produit_2', price=200)

session.add(produit1),
session.add(produit2)
session.commit()

results = session.query(Product).all()
for ind, product in enumerate(results):
    print('ind -', product.id)
    print('name - ', product.name)
    print('price -', product.price)

session.close()