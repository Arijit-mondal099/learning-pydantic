from pydantic import BaseModel, field_validator, model_validator, computed_field
from typing import List

class User(BaseModel):
    username: str
    password: str
    confirm_password: str
    
    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 4:
            raise ValueError("Username must be 4 characters long!")
        return value
    
    @model_validator(mode="after")
    def validate_password(cls, values):
        if values.confirm_password != values.password:
            raise ValueError("Password does not match!")
        return values
    
class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

class Cart(BaseModel):
    products: List[Product]
    
    @computed_field
    @property
    def total_price(self) -> float:
        return sum(product.price * product.quantity for product in self.products)
    
    @computed_field
    @property
    def total_products(self) -> int:
        return len(self.products)

product1 = Product(
    id=1,
    name="Keyboard",
    price=1000,
    quantity=2
)

product2 = Product(
    id=2,
    name="Mouse",
    price=500,
    quantity=3
)

user_cart = Cart(products=[product1, product2])
print(user_cart.model_dump())
