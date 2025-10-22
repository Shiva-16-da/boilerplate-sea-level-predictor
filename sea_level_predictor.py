import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.intercept + res.slope * x_pred

    new_df = df[df['Year'] >= 2000]
    res2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.intercept + res2.slope * x_pred2

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Original Data")
    ax.plot(x_pred, y_pred, 'r', label="Best Fit Line 1880-2050")
    ax.plot(x_pred2, y_pred2, 'g', label="Best Fit Line 2000-2050")
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig
