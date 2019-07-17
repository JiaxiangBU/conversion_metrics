'''Plot conversion rates and related metrics.'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotting_conv(dataframe, x_rotation_degree = 45, x_label_size = 12):
    for column in dataframe:
        # Plot column by dataframe's index
        plt.plot(dataframe.index, dataframe[column])
        plt.title('Daily ' + str(column) + ' conversion rate\n', 
                  size = 16)
        plt.ylabel('Conversion rate', size = 14)
        plt.xlabel('Date', size = x_label_size)
        plt.xticks(rotation = x_rotation_degree)
        # Show plot
        plt.show()
        plt.clf()
