import numpy as np
from matplotlib.dates import date2num
import warnings
from .flood import stations_level_over_threshold


def polyfit(dates: list, levels: list, p: int):
    """Function that takes in the dates, level and degree, and polyfits
    the data to the p th degree, returns a numpy.poly1d object and the dateshift"""

    # warning if polynomial degree is too high
    with warnings.catch_warnings():
        warnings.filterwarnings("error")
        try:
            dates = date2num(dates)
            date_shift = dates[0]
            p_coeff = np.polyfit(dates - date_shift, levels, p)
            poly = np.poly1d(p_coeff)
            return poly, date_shift

        except np.RankWarning:
            warnings.warn("Warning the degree is too high for the size of data given.\nPlease use a lower degree")


def sort_risk_level(stations):
    '''Sorts stations into 4 levels of risk Severe, high, moderate with
    relative river levels of 10, 5 and 3 repectively.'''
    severe, high, moderate = 10, 5, 3

    stationsSevere = stations_level_over_threshold(stations, severe)
    stationsHigh = stations_level_over_threshold(stations, high)
    stationsModerate = stations_level_over_threshold(stations, moderate)

    stationsSorted = []
    for station in stations:
        stationName = station.name
        stationCoOrd = station.coord
        stationTown = station.town
        rel_water_level = station.relative_water_level()

        if rel_water_level is None:
            # invalid stations
            continue
        else:
            rel_water_level = round(rel_water_level, 3)

        stationInfo = '{}, {},<br>Relative Water Level : {}'.format(stationName, stationTown, rel_water_level)
        """
        remeber stations_level_over_threshold returns an array of
        tuples containing station objects and rel_level, we
        only want a list of station objects
        """
        if station in [tuple[0] for tuple in stationsSevere]:
            station.risk_level = 'S'
            stationSeverity = 'S'
        elif station in [tuple[0] for tuple in stationsHigh]:
            station.risk_level = 'H'
            stationSeverity = 'H'
        elif station in [tuple[0] for tuple in stationsModerate]:
            station.risk_level = 'M'
            stationSeverity = 'M'
        else:
            station.risk_level = 'L'
            stationSeverity = 'L'

        stationData = [stationInfo, stationCoOrd, stationSeverity]
        stationsSorted.append(stationData)

    return stationsSorted
