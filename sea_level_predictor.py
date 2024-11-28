import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_range = np.linspace(1880, 2050, 100)
    y_range = slope * x_range + intercept
    ax.plot(x_range, y_range, color='red', label="1880-2050 Regression")

    # Create second line of best fit
    x_filtered = x[x >= 2000]
    y_filtered = y[x >= 2000]
    slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = linregress(x_filtered, y_filtered)
    x_range_2 = np.linspace(2000,2050,100)
    y_range_2 = slope_2 * x_range_2 + intercept_2
    ax.plot(x_range_2, y_range_2, color='blue', label="2000-2050 Regression")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
