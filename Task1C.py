from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()
coord_camcity = (52.2053, 0.1218)

arr = stations_within_radius(stations, coord_camcity, 10)
sorted_arr = sorted(arr)  # sort alphabetically


print(sorted_arr)


def test_check():
    """testing function to check if result
    is correct"""
    assert sorted_arr == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
                          'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
                          'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
