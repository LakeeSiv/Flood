#This calls the two functions defined in task 1d and displays the data

from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list

stations = build_station_list()

riversWithStation = rivers_with_station(stations)
print(len(riversWithStation))
sortedList = sorted(riversWithStation)
print(sortedList[:10])

stationsByRiver = stations_by_river(stations)
riverAire = list()
riverCam = list()
riverThames = list()
for station in stationsByRiver['River Aire']:
    riverAire.append(station.name)
    riverAire.sort()

for station in stationsByRiver['River Cam']:
    riverCam.append(station.name)
    riverCam.sort()

for station in stationsByRiver['River Thames']:
    riverThames.append(station.name)
    riverThames.sort()

print(riverAire,'\n', riverCam, '\n', riverThames)

    
