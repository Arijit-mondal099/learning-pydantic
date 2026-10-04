from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=16)
    depertment: str = Field(default="general")
    salary: float = Field(..., ge=10000)

emp_1 = Employee(id=1, name="arijit mondal", salary=12000)
print(emp_1)
