import numpy as np
from matplotlib.dates import date2num
import warnings


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
