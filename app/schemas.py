from pydantic import BaseModel, ConfigDict

class CustomerBase(BaseModel):
    name: str
    email: str

class Customer(CustomerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProductBase(BaseModel):
    name: str
    price: float

class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class OrderBase(BaseModel):
    customer_id: int
    product_id: int

class Order(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
