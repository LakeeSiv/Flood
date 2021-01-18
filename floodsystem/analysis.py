import numpy as np
from matplotlib.dates import date2num
from datetime import datetime


def polyfit(dates :list, levels :list, p: int):

    dates = date2num(dates)
    date_shift = dates[0]
    p_coeff = np.polyfit(dates - date_shift, levels , p)
    poly = np.poly1d(p_coeff)

    return poly, date_shift

