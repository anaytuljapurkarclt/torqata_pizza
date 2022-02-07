import datetime

from pydantic import BaseModel

class orderBase(BaseModel):
    customer_id: int
    type: str
    qty: int
    retail_price: float
    order_date: datetime.datetime
    load_ts: datetime.datetime

    class Config:
        orm_mode = True