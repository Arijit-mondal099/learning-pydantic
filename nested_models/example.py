from pydantic import BaseModel, Field, field_validator

class Address(BaseModel):
    dist: str = Field(..., min_length=2)
    ps: str = Field(..., min_length=2)
    vill: str = Field(..., min_length=2)
    po: str = Field(..., min_length=2)
    pin_code: str

    @field_validator("pin_code")
    def validate_pin_code(cls, value):
        if len(value) != 6:
            raise ValueError("Pin code must be 6 characters long!")

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=4, max_length=16)
    address: Address       

user_address = Address(
    dist="murshidabad",
    ps="beldanga",
    vill="madda",
    po="madda",
    pin_code="123456"
)

user = User(
    id=1,
    name="arijit mondal",
    address=user_address
)
