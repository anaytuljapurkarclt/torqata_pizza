import uvicorn
from fastapi import FastAPI
from app.schemas.orderBase import orderBase
from app.models.orders import orders
from app import db_conn

app = FastAPI()


s = next(db_conn.session_conn())

@app.post("/createOrdersRecords/", response_model=orderBase)
def getOrdersRecords(order: orderBase):
    db_order = orders(customer_id=order.customer_id, type=order.type, qty=order.qty,retail_price=order.retail_price, order_date=order.order_date
                      , load_ts=order.load_ts)
    s.add(db_order)
    s.commit()
    return db_order

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)