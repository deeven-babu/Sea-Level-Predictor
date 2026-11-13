
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # First line of best fit: 1880 to 2050
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = pd.Series(range(1880, 2051))

    predictions = intercept + slope * years

    ax.plot(years, predictions, 'r')

    # Second line of best fit: 2000 to 2050
    recent_data = df[df['Year'] >= 2000]

    slope, intercept, r_value, p_value, std_err = linregress(
        recent_data['Year'],
        recent_data['CSIRO Adjusted Sea Level']
    )

    recent_years = pd.Series(range(2000, 2051))

    recent_predictions = intercept + slope * recent_years

    ax.plot(recent_years, recent_predictions, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return axes for testing
    plt.savefig('sea_level_plot.png')

    return ax
