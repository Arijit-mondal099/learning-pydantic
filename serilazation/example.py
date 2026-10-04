from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Address(BaseModel):
    city: str
    pin_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    created_at: datetime
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%D %H:%M:%S")}
    )

user = User(
    id=1,
    name="arijit mondal",
    address=Address(
        city="kolkata",
        pin_code="742133"
    ),
    created_at=datetime(2026, 8, 20, 21, 44)
)

# Normal user
print(user)

# With model_dump -> return dict of data
print(user.model_dump())

# With model_dump_json -> return json string of data
print(user.model_dump_json())
