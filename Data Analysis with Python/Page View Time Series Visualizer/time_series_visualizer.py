import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#// Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('Data Analysis with Python\\Page View Time Series Visualizer\\fcc-forum-pageviews.csv', index_col='date') #! Change for Replit !
# df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
# print(df.head())

#// Clean data
# print(df.shape[0])
q_low = df["value"].quantile(0.025)
q_high = df["value"].quantile(0.975)
df = df.loc[(df["value"] >= q_low) & (df["value"] <= q_high)]
# print(df.shape[0])
# print(int(df.count(numeric_only=True)))

def draw_line_plot():
    #// Draw line plot
    fig, axes = plt.subplots(figsize=(18,6))
    axes.plot(df)
    axes.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python\\Page View Time Series Visualizer\\plots\\line_plot.png') #! Change for Replit !
    # fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    #// Copy and modify data for monthly bar plot
    df_cop = df.copy()
    df_cop['year'] = pd.DatetimeIndex(df_cop.index).year
    df_cop['month'] = pd.DatetimeIndex(df_cop.index).month
    df_cop['month_name'] = pd.DatetimeIndex(df_cop.index).month_name()
    df_bar = df_cop.groupby(['year', 'month', 'month_name'])['value'].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_pivot = df_bar.pivot(index='year', columns='month', values='value')
    df_pivot = df_pivot.reindex(columns=range(1, 13))
    df_pivot.columns = [calendar.month_name[i] for i in range(1, 13)]
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python\\Page View Time Series Visualizer\\plots\\bar_plot.png') #! Change for Replit !
    # fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    #// Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    #// Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=months_order)
    
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[0].set_xlabel('Year')
    axes[1].set_xlabel('Month')
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python\\Page View Time Series Visualizer\\plots\\box_plot.png') #! Change for Replit !
    # fig.savefig('box_plot.png')
    return fig

if __name__=="__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
