from floodsystem import datafetcher, flood, plot, station, stationdata
from datetime import timedelta


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    stations = station.consistant_typical_range_stations(stations)

    top5Stations = flood.stations_highest_rel_level(stations, 5)
    top5StationsDates = []
    top5StationsLevels = []
    for top5station in top5Stations:
        stationDates, stationLevels = datafetcher.fetch_measure_levels(top5station.measure_id, timedelta(days=10))
        top5StationsDates.append(stationDates)
        top5StationsLevels.append(stationLevels)

    plot.plot_water_levels(top5Stations, top5StationsDates, top5StationsLevels)


if __name__ == "__main__":
    run()
