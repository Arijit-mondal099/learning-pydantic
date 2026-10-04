from pydantic import BaseModel

# Pydantic model/schema
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_admin: bool = False # Default value

# Create users via model
user_1 = User(id=1, name="arijit", email="arijitm717@gmail.com", password="12345678")
user_input = {"id": 2, "name": "pritam", "email": "mondalpritam777888999@gmail.com", "password": "12345678"}
user_2 = User(**user_input)

print(user_1)
print(user_2)
