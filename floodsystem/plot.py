import matplotlib.pyplot as plt
from .analysis import polyfit
from matplotlib.dates import date2num


def plot_water_levels(stations, dates, levels):

    for station in levels:
        for i in station:
            if not isinstance(i, float):
                index = levels.index(station)
                del dates[index]
                del stations[index]
                levels.remove(station)
                print('The number {} highest station contained curropted date. This station will not be plotted'.format(index))
                break

    if len(stations) > 2:
        y = int(round(len(stations) / 2 + .1))
        x = int(round(len(stations) / y))
        fig, axs = plt.subplots(x, y, figsize=(12, 6))
        for i in range(int(round(len(stations) / 2 + .1))):
            axs[0, i].plot(dates[i], levels[i])
            axs[0, i].axhline(stations[i].typical_range[0], color='r', ls='--')
            axs[0, i].axhline(stations[i].typical_range[1], color='r', ls='--')
            axs[0, i].set_title(stations[i].name)
            axs[0, i].set_xlabel('Dates')
            axs[0, i].set_ylabel('Water Level(m)')
            axs[0, i].tick_params(axis='x', rotation=30)

        for i in range(int(round(len(stations) / 2 - .1))):
            axs[1, i].plot(dates[i + int(round(len(stations) / 2 + .1, 0))],
                           levels[i + int(round(len(stations) / 2 + .1, 0))])
            axs[1, i].set_title(stations[i + int(round(len(stations) / 2 + .1, 0))].name)
            axs[1, i].axhline(stations[i].typical_range[0], color='r', ls='--')
            axs[1, i].axhline(stations[i].typical_range[1], color='r', ls='--')
            axs[1, i].set_xlabel('Dates')
            axs[1, i].set_ylabel('Water Level(m)')
            axs[1, i].tick_params(axis='x', rotation=30)

        fig.tight_layout()

        fig.show()
        plt.show()

    elif len(stations) == 2:
        y = len(stations)
        fig, axs = fig, axs = plt.subplots(1, y, figsize=(12, 6))

        for i in range(int(len(stations))):
            axs[i].plot(dates[i], levels[i])
            axs[i].axhline(stations[i].typical_range[0], color='r', ls='--')
            axs[i].axhline(stations[i].typical_range[1], color='r', ls='--')
            axs[i].set_title(stations[i].name)
            axs[i].set_xlabel('Dates')
            axs[i].set_ylabel('Water Level(m)')
            axs[i].tick_params(axis='x', rotation=30)

        fig.tight_layout()

        fig.show()
        plt.show()

    elif len(stations) == 1:
        plt.plot(dates[0], levels[0])
        plt.title(stations[0].name)
        plt.axhline(stations[0].typical_range[0], color='r', ls='--')
        plt.axhline(stations[0].typical_range[1], color='r', ls='--')
        plt.ylabel('Dates')
        plt.xlabel('Water Level(m)')
        plt.xticks(rotation=60)
        plt.tight_layout()
        plt.show()

    else:
        raise RuntimeError('All Stations Contained Corrupted Data')


def plot_water_level_with_fit(stations, dates, levels, p):
    """Can take a single station object and its data, or can
    take a list of station objects, with its list of data, then plots
    the graph of the data along side a polyfitted graph with degree p  """

    plt.style.use("seaborn")

    # first handle list of stations
    if isinstance(stations, list):

        cols = 3
        N = len(stations)

        rows = N // cols + N % cols

        position = range(1, N + 1)

        fig = plt.figure(1)

        # iterate through each stations and plot
        for i in range(N):
            station = stations[i]
            ax = fig.add_subplot(rows, cols, position[i])
            ax.axhline(station.typical_range[0], color='b', ls='--', label="low range")
            ax.axhline(station.typical_range[1], color='r', ls='--', label="high range")
            ax.plot(dates[i], levels[i], color="black", label="Water level")

            poly, d0 = polyfit(dates[i], levels[i], p)
            ax.plot(dates[i], poly(date2num(dates[i]) - d0), label="Fitted water level")
            ax.set_title(station.name)
            ax.set_xlabel('Dates')
            ax.set_ylabel('Water Level(m)')
            ax.tick_params(axis='x', rotation=30)
            ax.set_xbound(dates[i][0], dates[i][-1])
            ax.legend(loc="upper left", prop={"size": 7}, fancybox=True, framealpha=0.5)
        plt.tight_layout(pad=0)

    # now handle single station object
    else:
        station = stations
        plt.axhline(station.typical_range[0], color='b', ls='--', label="low range")
        plt.axhline(station.typical_range[1], color='r', ls='--', label="high range")
        plt.plot(dates, levels, color="black", label="Water level")

        poly, d0 = polyfit(dates, levels, p)
        plt.plot(dates, poly(date2num(dates) - d0), label="Fitted water level")
        plt.title(station.name)
        plt.xlabel('Dates')
        plt.ylabel('Water Level(m)')
        plt.tick_params(axis='x', rotation=30)
        plt.xlim(dates[-1], dates[0])

        plt.legend()

    plt.show()
