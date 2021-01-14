"""Tests the module Geo to ensure its functions return the desired information"""

from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation


def generate_test_station():
    '''Generate a list of MonitoringStation objects to use for testing'''
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ("some station", "Another Station", "Station 3")
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = ("River X", "River Y", "River Z")
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label[0], coord, trange, river[0], town)
    s2 = MonitoringStation(s_id, m_id, label[1], coord, trange, river[1], town)
    s3 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[0], town)
    s4 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[1], town)
    s5 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[1], town)
    s6 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[2], town)
    s7 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[2], town)

    return [s1, s2, s3, s4, s5, s6, s7]


def test_rivers_with_station():
    """Test that the function returns the correct data without duplicates"""

    stations = generate_test_station()

    assert rivers_with_station(stations) == {"River X", "River Y", "River Z"}


def test_stations_by_river():
    """Test that the function returns the correct data"""

    stations = generate_test_station()
    s1, s2, s3, s4, s5, s6, s7 = stations

    assert stations_by_river(stations) == {'River X': [s1, s3], 'River Y': [s2, s4, s5], 'River Z': [s6, s7]}


def test_rivers_by_station_number():
    '''Test that the function works as required'''

    stations = generate_test_station()

    assert rivers_by_station_number(stations, 1) == [('River Y', 3)]
    assert rivers_by_station_number(
        stations, 2) == [
        ('River Y', 3), ('River X', 2), ('River Z', 2)] or [
            ('River Y', 3), ('River Z', 2), ('River X', 2)]
