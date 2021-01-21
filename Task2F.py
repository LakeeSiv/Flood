"""
-------------------------------------------IMPORTANT--------------------------------------------------
It was found that sometimes the water level data was inconsistant, for example, once a station returned
an array of numbers and lists, which is inocrrect, as it should only return an array of numbers
"""


from floodsystem import datafetcher, flood, plot, station, stationdata
from datetime import timedelta


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    stations = station.consistant_typical_range_stations(stations)

    top10Stations = flood.stations_highest_rel_level(stations, 10)

    topStations = []
    topStationsDates = []
    topStationsLevels = []
    counter = 0
    NUMBER_PLOTS = 5

    for st in top10Stations:
        stationDates, stationLevels = datafetcher.fetch_measure_levels(st.measure_id, timedelta(days=2))

        # only consistant ones get saved
        if all(isinstance(x, (int, float)) for x in stationLevels):
            counter += 1
            topStations.append(st)
            topStationsDates.append(stationDates)
            topStationsLevels.append(stationLevels)
        if counter == NUMBER_PLOTS:
            break

    # single object input

    plot.plot_water_level_with_fit(topStations[0], topStationsDates[0], topStationsLevels[0], 4)

    # list of object input
    plot.plot_water_level_with_fit(topStations, topStationsDates, topStationsLevels, 4)


if __name__ == "__main__":
    run()
