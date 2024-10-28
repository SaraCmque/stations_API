from pydantic import BaseModel, Field

class Location(BaseModel):
    """
    Data model for representing the geographical location of a Station.
    
    Attributes:
        latitude (float): 
            The latitude of the station in decimal degrees.
            Example: 40.7128
        longitude (float): 
            The longitude of the station in decimal degrees.
            Example: -74.0060
    """
    latitude: float = Field(..., example=40.7128, description="The latitude of the station in decimal degrees.")
    longitude: float = Field(..., example=-74.0060, description="The longitude of the station in decimal degrees.")

class StationCreate(BaseModel):
    """
    Data model for creating a new Station.
    
    This model is used when a new Station is being created.

    Attributes:
        name (str): 
            The name of the station.
            Example: "Estación Central"
        location (Location): 
            The geographical location of the station, including latitude and longitude.
    """
    name: str = Field(..., example="Estación Central", description="The name of the station.")
    location: Location = Field(..., description="The geographical location of the station, including latitude and longitude.")

class StationResponse(BaseModel):
    """
    Model for an existing station.
    
    Attributes:
        id (int): Unique identifier of the station.
        name (str): Name of the station.
        location (Location): Geographical location of the station.
    """
    id: int
    name: str
    location: Location

    class Config:
        orm_mode = True