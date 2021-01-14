from .station import consistant_typical_range_stations


def stations_level_over_threshold(stations: list, tol: float) -> list:
    """function takes in stations and returns a list of tuples contating station and
    relative water lever where the relative water level greater than tol """
    stations = consistant_typical_range_stations(stations)
    res_list = []

    for station in stations:
        if station.relative_water_level() > tol:
            res_list.append((station, station.relative_water_level()))

    return res_list
