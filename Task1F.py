from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
inconsistant_stations = inconsistent_typical_range_stations(stations)

inconsistant_stations = sorted([station.name for station in inconsistant_stations])

print(inconsistant_stations)
