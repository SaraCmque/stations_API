from sqlalchemy import Column, Integer, String, Float
from app.api.config.database import Base

class Station(Base):
    """
    SQLAlchemy model for the 'stations' table.
    
    Attributes:
        id (int): Unique identifier for the station.
        name (str): Name of the station.
        latitude (float): Latitude in decimal degrees.
        longitude (float): Longitude in decimal degrees.
    """
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment="Unique identifier for the station.")
    name = Column(String, nullable=False, index=True, comment="Name of the station.")
    latitude = Column(Float, nullable=False, comment="Latitude in decimal degrees.")
    longitude = Column(Float, nullable=False, comment="Longitude in decimal degrees.")

