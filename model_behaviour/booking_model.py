from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float = Field(..., gt=0)
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.rate_per_night * self.nights
