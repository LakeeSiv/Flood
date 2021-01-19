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
    '''Sorts stations into 4 levels of risk Severe, high, moderate and low with
    relative river levels of 3.5, 2.5, 2 and 1 repectively.'''

    stationsSevere = stations_level_over_threshold(stations, 3.5)
    stationsHigh = stations_level_over_threshold(stations, 2.5)
    stationsModerate = stations_level_over_threshold(stations, 2.0)
    # stationsLow = stations_level_over_threshold(stations, 1.0)
    stationsSorted = []
    for station in stations:
        stationName = station.name
        stationCoOrd = station.coord
        stationTown = station.town
        stationInfo = '{}, {}'.format(stationName, stationTown)
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