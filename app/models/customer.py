from sqlalchemy import Column, Integer, VARCHAR, CHAR

from app.models.base import Base

class customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(VARCHAR(100), nullable=False)
    address = Column(VARCHAR(200), nullable=False)
    city = Column(VARCHAR(50), nullable=False)
    state = Column(CHAR(2), nullable=False)
    zip_code = Column(CHAR(5), nullable=False)

    __table_args__ = {"schema": "torqata_data_ip"}