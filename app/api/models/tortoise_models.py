from tortoise import fields
from tortoise.models import Model

class Station(Model):
    """
    Tortoise ORM model for the 'stations' table.
    
    Attributes:
        id (int): Unique identifier for the station.
        name (str): Name of the station.
        latitude (float): Latitude in decimal degrees.
        longitude (float): Longitude in decimal degrees.
    """
    id = fields.IntField(pk=True, index=True, description="Unique identifier for the station.")
    name = fields.CharField(max_length=255, null=False, index=True, description="Name of the station.")
    latitude = fields.FloatField(null=False, description="Latitude in decimal degrees.")
    longitude = fields.FloatField(null=False, description="Longitude in decimal degrees.")

    class Meta:
        table = "stations"
