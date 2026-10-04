from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import List, Annotated

class User(BaseModel):
    username: Annotated[str, Field(..., title="Username", description="The username of the user", examples=["arijit", "babai"])]
    password: Annotated[str, Field(..., min_length=8, max_length=16)]
    confirm_password: Annotated[str, Field(..., min_length=8, max_length=16)]
    
    # validation -> type coercion -> after (default)
    # validation -> before -> type coercion
    
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
    name: Annotated[str, Field(..., min_length=4, max_length=16)]
    price: Annotated[float, Field(..., gt=0)]
    quantity: Annotated[int, Field(..., gt=0)]

class Cart(BaseModel):
    products: Annotated[List[Product], Field(..., max_length=5)]
    
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
