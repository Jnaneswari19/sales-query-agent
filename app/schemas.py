# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class CustomerBase(BaseModel):
    name: str
    region: Optional[str] = None
    segment: Optional[str] = None

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
    date: str

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
