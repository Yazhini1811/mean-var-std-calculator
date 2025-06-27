import pandas as pd

# Load data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filter out top and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
import matplotlib.pyplot as plt

def draw_line_plot():
    # Create a copy of the dataframe
    df_copy = df.copy()

    # Plot line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_copy.index, df_copy['value'], color='tab:blue', linewidth=1.0)

    # Set labels and title
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel='Date',
           ylabel='Page Views')

    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig
def draw_bar_plot():
    # Create a copy of the dataframe
    df_copy = df.copy()

    # Resample data to get monthly averages
    df_copy = df_copy.resample('M').mean()

    # Plot bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    df_copy['value'].plot(kind='bar', ax=ax, color='tab:green')

    # Set labels and title
    ax.set(title='Average Daily Page Views per Month',
           xlabel='Month',
           ylabel='Average Page Views')

    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig
import seaborn as sns

def draw_box_plot():
    # Create a copy of the dataframe
    df_copy = df.copy()

    # Extract year and month from the index
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()

    # Set up the matplotlib figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_copy, ax=ax1)
    ax1.set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')

    # Month-wise box plot
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.boxplot(x='month', y='value', data=df_copy, ax=ax2, order=month_order)
    ax2.set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')

    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig
