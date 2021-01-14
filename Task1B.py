from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
coord_camcity = (52.2053, 0.1218)
stations_list = stations_by_distance(stations, coord_camcity)


def convert(x):
    """
    function takes x which is an array in the form

    x = [(station, distance), ......] // note station is an object

    and returns an array in the form of

    [(station.name, station.town, distance ), ......]
    """

    res_arr = []

    for tuple in x:
        res_arr.append((tuple[0].name, tuple[0].town, tuple[1]))

    return res_arr


converted_list = convert(stations_list)

closest_10 = converted_list[:10]
furthest_10 = converted_list[-10:]

print(f"{closest_10}\n{furthest_10}")
