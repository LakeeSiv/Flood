from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


stations = build_station_list()


def run():
    update_water_levels(stations)
    topStations = stations_highest_rel_level(stations, 10)
    for i in topStations:
        print('{}  {}'.format(i.name, i.relative_water_level()))


if __name__ == '__main__':
    run()
