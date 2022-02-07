from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Float, DateTime
from sqlalchemy.sql import func
from app.models.base import Base
from app.models import customer

class orders(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True,autoincrement=True)
    customer_id = Column(Integer, ForeignKey("torqata_data_ip.customer.customer_id"), nullable=False)
    type = Column(VARCHAR(20), nullable=False)
    qty = Column(Integer, nullable=False)
    retail_price = Column(Float, nullable=False)
    order_date = Column(DateTime,nullable=False)
    load_ts = Column(DateTime,nullable=False)
    # Uncomment when switching to Prod
    # order_date = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = {"schema": "torqata_data_ip"}