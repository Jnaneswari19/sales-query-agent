from datetime import datetime
from app.db import Base, engine, SessionLocal
from app.models import Customer, Product, Order

def init_db():
    Base.metadata.drop_all(bind=engine)   # reset schema
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    alice = Customer(name="Alice", email="alice@example.com")
    bob = Customer(name="Bob", email="bob@example.com")

    laptop = Product(name="Laptop", price=1200.0)
    phone = Product(name="Phone", price=800.0)

    db.add_all([alice, bob, laptop, phone])
    db.commit()

    order1 = Order(customer_id=alice.id, product_id=laptop.id, timestamp=datetime.now())
    order2 = Order(customer_id=bob.id, product_id=phone.id, timestamp=datetime.now())

    db.add_all([order1, order2])
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
