import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('epa-sea-level.csv')
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = range(1880, 2051)
sea_levels_extended = [slope * year + intercept for year in years_extended]
plt.plot(years_extended, sea_levels_extended, label='Best Fit Line (1880-2050)')
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
plt.plot(years_extended, sea_levels_recent, label='Best Fit Line (2000-2050)', linestyle='--')
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.legend()
plt.savefig('sea_level_plot.png')
