from test_geo import generate_test_station
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


def test_stations_highest_rel_level():
    stations = generate_test_station()
    stations[0].typical_range, stations[0].latest_level = (0, 5), 2.5  # Station 1
    stations[1].typical_range, stations[1].latest_level = (0, 2.5), 2.5  # Station 2
    stations[2].typical_range, stations[2].latest_level = (0, 1), 0  # Station 3

    # all other stations are inconsistant

    over_thers_stations = stations_level_over_threshold(stations, 0.2)
    # Station 3 lower that thershold

    assert over_thers_stations[0][1] == 0.5
    assert over_thers_stations[1][1] == 1


def test_stations_highest_rel_level():
    stations = generate_test_station()
    stations[0].typical_range, stations[0].latest_level = (0.1, 0.5), 0.25
    stations[1].typical_range, stations[1].latest_level = (0.1, 1.5), 0.25
    stations[2].typical_range, stations[2].latest_level = (0.0, 2.5), 3.0
    stations[3].typical_range, stations[3].latest_level = (0.1, 0.5), 1.0
    stations[4].typical_range, stations[4].latest_level = (0.1, 5), 10.0
    stations[5].typical_range, stations[5].latest_level = (0.1, 0.5), 3.0
    stations[6].typical_range, stations[6].latest_level = (1.0, 0.5), 1.0
    [s1, s2, s3, s4, s5, s6, s7] = stations

    assert stations_highest_rel_level(stations, 2) == [s6, s4]
    assert len(stations_highest_rel_level(stations, 7)) != 7
    assert stations_highest_rel_level(stations, 6) == [s6, s4, s5, s3, s1, s2]


test_stations_highest_rel_level()
