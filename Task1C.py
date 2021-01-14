from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    coord_camcity = (52.2053, 0.1218)

    arr = stations_within_radius(stations, coord_camcity, 10)
    sorted_arr = sorted(arr)  # sort alphabetically

    print(sorted_arr)


if __name__ == "__main__":
    run()
