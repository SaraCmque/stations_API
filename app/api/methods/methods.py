from app.api.models.tortoise_models import Station
from app.api.models.models import StationCreate, StationResponse, Location
from typing import List
from tortoise.expressions import RawSQL

async def create_station(station_data: StationCreate) -> StationResponse:
    """
    Creates a new station in the database.

    Args:
        station_data (StationCreate): Data of the station to create.

    Returns:
        StationResponse: The created station object.
    """
    new_station = await Station.create(
        name=station_data.name,
        latitude=station_data.location.latitude,
        longitude=station_data.location.longitude
    )

    return StationResponse(
        id=new_station.id,
        name=new_station.name,
        location=Location(latitude=new_station.latitude, longitude=new_station.longitude)
    )

async def get_stations() -> List[StationResponse]:
    """
    Retrieves all stations from the database.

    Returns:
        List[StationResponse]: A list of station objects.
    """
    stations = await Station.all()
    return [
        StationResponse(
            id=station.id,
            name=station.name,
            location=Location(latitude=station.latitude, longitude=station.longitude)
        )
        for station in stations
    ]

async def get_station_by_id(station_id: int):
    """
    Retrieves a station by its ID.

    Args:
        station_id (int): ID of the station to retrieve.

    Returns:
        Station or None: The station object if found, else None.
    """
    return await Station.filter(id=station_id).first()


async def get_closest_station(station_id: int):
    """
    Finds the closest station to a given station ID.

    Args:
        station_id (int): ID of the reference station.

    Returns:
        Station or None: The closest station object, or None if the reference station doesn't exist.
    """
    base_station = await Station.filter(id=station_id).first()
    if not base_station:
        return None

    closest_station = await Station.exclude(id=station_id).annotate(
    distance=RawSQL(
        f"sqrt(pow(latitude - {base_station.latitude}, 2) + pow(longitude - {base_station.longitude}, 2))"
    )
).order_by("distance").first()

    return closest_station