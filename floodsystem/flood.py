


def stations_highest_rel_level(stations, N):
    """Returns a list of N MonitoringStation objects ordered from highest to lowest risk"""

     stationByHighestLevel = sorted(stations, key = self.relative_water_level) #Hoping this will work we shall see

     NstationByLevel = stationByHighestLevel[:N]
     return NstationByLevel

    

stations = build_station_list()
print(stations_highest_rel_level(stations, 10))
