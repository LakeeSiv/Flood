# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self) -> bool:
        """checks to see if the typical range
        is consistant.
        Inconsistant when: range is empty, or high range < low range"""

        if self.typical_range is None:
            return False
        elif self.typical_range[1] < self.typical_range[0]:
            return False
        else:
            return True

    def relative_water_level(self) -> float:
        """Function that takes the latest water level and maps it to a number between 0-1,
            where
            1: highest typical range
            0: lowest typical range"""
        if self.typical_range_consistent() is True:  # check for consistant trange
            high = self.typical_range[1]
            low = self.typical_range[0]

            if self.latest_level is None:
                return None
            else:
                return (self.latest_level - low) / (high - low)
        else:
            return None


def inconsistent_typical_range_stations(stations):
    """function takes in a list of stations and returns the list of
    stations with inconsistant typical ranges """

    inconsistant_list = []

    for station in stations:
        if station.typical_range_consistent() is False:
            inconsistant_list.append(station)

    return inconsistant_list


def consistant_typical_range_stations(stations):
    """function takes in a list of stations and returns the list of
    stations with consistant typical ranges """

    consistant_list = []

    for station in stations:
        if station.typical_range_consistent() is True:
            consistant_list.append(station)

    return consistant_list
