from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    city: str

class Customer(CustomerBase):
    id: int
    class Config:
        from_attributes = True  

class ProductBase(BaseModel):
    name: str
    price: float

class Product(ProductBase):
    id: int
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_id: int

class Order(OrderBase):
    id: int
    class Config:
        from_attributes = True

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int

class OrderItem(OrderItemBase):
    id: int
    class Config:
        from_attributes = True
