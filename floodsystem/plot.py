import matplotlib.pyplot as plt
# from .analysis import polyfit


def plot_water_levels(stations, dates, levels):

    if len(stations) > 1:
        y = int(round(len(stations) / 2 + .1))
        x = len(stations) - y
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

# def plot_water_level_with_fit(station, dates, levels, p):

#     """  """
#     if
#     poly, d0 = polyfit()
