# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """ Function to calcuate the distannce between a station
    and the coordinate p, and returns a list of the station and
    the distance"""

    resulting_arr = []

    for station in stations:
        coord = station.coordinate
        distance = haversine(coord,p)

        resulting_arr.append((station, distance))

    return resulting_arr

