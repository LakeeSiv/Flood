#Tests the file Geos respective modules

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    #test that it returns a set with no duplicates and that it contains all rivers
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ("some station", "Another Station", "Station 3")
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = ("River X", "River Y")
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label[0], coord, trange, river[0], town)
    s2 = MonitoringStation(s_id, m_id, label[1], coord, trange, river[1], town)
    s3 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[0], town)

    stations = (s1, s2, s3)

    assert rivers_with_station(stations) == {"River X", "River Y"}

def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ("some station", "Another Station", "Station 3")
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = ("River X", "River Y")
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label[0], coord, trange, river[0], town)
    s2 = MonitoringStation(s_id, m_id, label[1], coord, trange, river[1], town)
    s3 = MonitoringStation(s_id, m_id, label[2], coord, trange, river[0], town)

    stations = (s1, s2, s3)

    assert stations_by_river(stations) == {'River X': ['some station', 'Station 3'], 'River Y': ['Another Station']}

