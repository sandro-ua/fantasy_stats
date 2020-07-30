import numpy as np
import matplotlib.pyplot as plt


class Plot:

    def show_plot(self, teams, points):
        plt.suptitle('EPL FANTASY 2019-2020')
        max = 2000
        y_pos = np.arange(len(teams))

        #Color
        colors = plt.cm.Dark2(range(6))
        y = teams.index
        width = points.values


        # Create horizontal bar
        plt.xlabel('points')
        plt.barh(y_pos, points)

        # Create names on the y-axis
        plt.ylabel('teams')
        plt.yticks(y_pos, teams)






        # Show graphic
        plt.show()
