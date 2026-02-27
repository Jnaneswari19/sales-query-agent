from app.db import Base, engine
from app.models import Customer, Product, Order, OrderItem

DATABASE_URL = "sqlite:///./data/sales.db"

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sales = Column(Integer)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    order_date = Column(Date)
    amount = Column(Float)

# Create DB + tables
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

# Seed sample data
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

session.add_all([
    Customer(name="Alice", state="New York"),
    Customer(name="Bob", state="California"),
    Product(name="Laptop", sales=1200),
    Product(name="Phone", sales=800),
    Order(customer_id=1, product_id=1, order_date="2024-01-15", amount=1200),
    Order(customer_id=2, product_id=2, order_date="2024-01-20", amount=800),
])

session.commit()
session.close()
print("✅ Database initialized with sample data")
