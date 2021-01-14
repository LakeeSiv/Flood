# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import *  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """ Function to calcuate the distance between a station
    and the coordinate p, and returns a list of the station and
    the distance"""

    resulting_arr = []

    for station in stations:
        coord = station.coord
        distance = haversine(coord, p)

        resulting_arr.append((station, distance))

    return sorted_by_key(resulting_arr, 1, reverse=False)


def stations_within_radius(stations, centre, r):
    """
    Function returns a list of stations which are with a radius r of
    the centre coordinate
    """
    stations_distances = stations_by_distance(stations, centre)
    result_arr = []

    for tuple in stations_distances:
        if tuple[1] <= r:
            result_arr.append(tuple[0].name)
        else:
            break  # can break since the list is ordered by distance

    return result_arr


def rivers_with_station(stations):
    """
function that returns a set of the rivers with at least one station on them
if passed a list of MonitoringStation objects
"""

    riversWithStation = set()

    for station in stations:
        if station.river is not None:
            riversWithStation.add(station.river)

    return riversWithStation


def stations_by_river(stations):
    """
function that returns a dictionary of the stations on a river grouped by river name
if passed a list of MonitoringStation objects
"""

    riverStations = rivers_with_station(stations)

    stationsOnRiver = dict.fromkeys(riverStations)

    for station in stations:
        if stationsOnRiver[station.river] is not None:
            stationsOnRiver[station.river].append(station)
        else:
            stationsOnRiver[station.river] = [station]
    return stationsOnRiver


def rivers_by_station_number(stations, N):
    """Returns a list of N tuples containing the first N rivers by number of stations if given a list of
MonitoringStation objects and an integer N"""

    riverStations = stations_by_river(stations)
    sortedRiverStations = sorted(riverStations.items(), key=by_value_len)
    j = 0
    for i in sorted(riverStations.items(), key=by_value_len, reverse=True):
        z = (i[0], len(i[1]))
        sortedRiverStations[j] = z
        j += 1

    riverN = sortedRiverStations[:N]

    while True:
        try:
            if riverN[-1][1] == sortedRiverStations[N][1]:
                riverN.append(sortedRiverStations[N])
                N += 1
            else:
                break
        except IndexError:
            break

    return riverN
