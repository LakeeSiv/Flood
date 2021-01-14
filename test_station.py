# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def generate_test_station():
    '''Generate a list of MonitoringStation objects to use for testing'''

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5", "Station 6", "Station 7"]
    coord = [(0, 4), (0, 8), (0, 12), (0, 16), (0, 30), (0, 50), (0, 60)]
    trange = [None, (0, -1), (-2.3, 3.4445)]
    river = ("River X", "River Y", "River Z")
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label[0], coord[0], trange[0], river[0], town)
    s2 = MonitoringStation(s_id, m_id, label[1], coord[1], trange[1], river[1], town)
    s3 = MonitoringStation(s_id, m_id, label[2], coord[2], trange[2], river[0], town)
    s4 = MonitoringStation(s_id, m_id, label[3], coord[3], trange[2], river[1], town)
    s5 = MonitoringStation(s_id, m_id, label[4], coord[4], trange[2], river[1], town)
    s6 = MonitoringStation(s_id, m_id, label[5], coord[5], trange[2], river[2], town)
    s7 = MonitoringStation(s_id, m_id, label[6], coord[6], trange[2], river[2], town)

    return [s1, s2, s3, s4, s5, s6, s7]


def test_inconsistent_typical_range_stations():
    """test to see if this function return stations with inconsistant ranges"""

    stations = generate_test_station()
    inconst_stations = inconsistent_typical_range_stations(stations)

    for station in inconst_stations:
        assert station.typical_range_consistent() is False


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.typical_range_consistent() is False
