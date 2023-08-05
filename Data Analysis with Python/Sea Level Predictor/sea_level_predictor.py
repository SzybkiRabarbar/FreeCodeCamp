import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('Data Analysis with Python\\Sea Level Predictor\\epa-sea-level.csv') #! Change for Replit !
    # df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(df['Year'].min(), 2051)
    plt.plot(x, res.intercept + res.slope*x, 'r')

    # Create second line of best fit
    res = linregress(np.arange(2000,df['Year'].max()+1), df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x = np.arange(2000, 2051)
    plt.plot(x, res.intercept + res.slope*x, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('Data Analysis with Python\\Sea Level Predictor\\sea_level_plot.png') #! Change for Replit !
    # plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__=="__main__":
    draw_plot()