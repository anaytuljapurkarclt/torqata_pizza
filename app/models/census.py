from sqlalchemy import Column, VARCHAR, BIGINT, Float, CHAR

from app.models.base import Base

class CensusAdultPopByState(Base):
    __tablename__ = "census_adult_pop_by_state"
    __table_args__ = {"schema":"torqata_data_ip"}

    geographic_area = Column(VARCHAR(50), primary_key=True)
    total_resident_population = Column(BIGINT)
    total_resident_18yr_and_older = Column(BIGINT)
    percentage_population = Column(Float)
    state_abbr = Column(CHAR(2))