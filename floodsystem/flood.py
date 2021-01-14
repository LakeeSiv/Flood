from .station import consistant_typical_range_stations


def stations_level_over_threshold(stations: list, tol: float) -> list:
    """function takes in stations and returns a list of tuples contating station and
    relative water lever where the relative water level greater than tol """

    stations = consistant_typical_range_stations(stations)  # gets consistant stations

    res_list = []

    for station in stations:

        rel_level = station.relative_water_level()

        if rel_level is not None:  # ensures water level is not None
            if rel_level > tol:
                res_list.append((station, rel_level))

    return res_list
