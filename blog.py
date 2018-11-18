# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler
plt.rcParams['figure.figsize'] = 16, 12
#%cd '/home/omarsamhan/projects/t'

# Read in a single dataset which was extracted in the month of October 2018
df = pd.read_csv("calendar_oct.csv")

# count the number of missing values by row
df['NaN_count'] = df.isnull().sum(axis=1)

# Notice that any listing which isn't available has missing price information for those dates
# We delete those rows with any missing values since we're only interested in price information
# of the available options.
df = df.loc[df.NaN_count==0]

# Convert dates to Pandas datetime for the charts
df['date'] = pd.to_datetime(df['date'])
# Convert price to numbers
df['price'] = df['price'].replace('[\$,]','', regex=True).astype(float)
# Use a temporary date variable and assign it as the dataframe's index
df['date_'] = df['date']
df.set_index('date_', inplace=True)

# Find the orice at the 99th percentile
print(df.price.quantile(0.99))

# Create a scatter plot of all listing prices
f, ax = plt.subplots(1,1)
plt.ylabel('Price')
line = ax.scatter(list(df.date.values), list(df['price'].values), s =1, c = 'purple', label='Oct')
# Add legend to the plot
ax.legend(loc='best', title="Extraction date")
plt.show()

# Plot the most recent month by average price per day
df_m = df.groupby(['date'])['price'].agg([np.mean])
df_m = df_m.reset_index()
f, ax = plt.subplots(1,1)
plt.ylabel('Average Price')
ax.plot_date(df_m.date, df_m["mean"], c='purple', label='Oct', linestyle="-")
ax.legend(loc='best', title="Extraction date")
ax.label_outer()
plt.show()

ext_months = ['apr', 'may', 'jul', 'aug', 'sep', 'oct']
colours = ['blue','red','green','yellow','black','purple']

f, ax = plt.subplots(3,2,sharey=True,sharex=True)

# loop through each file
for i, (m, c) in enumerate(zip(ext_months,colours)):

    # Load the datasets
    df = pd.read_csv("calendar_" + m + ".csv")
    
    
    df['date'] = pd.to_datetime(df['date'])
    df['date_'] = df['date']
    df['price'] = df['price'].replace('[\$,]','', regex=True).astype(float)
    df.set_index('date_', inplace=True)
    
    # Calculate average prices by day
    df_m = df.groupby(['date'])['price'].agg([np.mean])
    df_m = df_m.reset_index()
    ax[i%3,i//3].plot_date(df_m.date, df_m["mean"], color=c, label=m.capitalize(), linestyle="-")
    ax[i%3,i//3].legend()
    ax[i%3,i//3].label_outer()
    
    # Filter the week for Christmas and New Year's
    mask = (df['date'] > '2018-12-23') & (df['date'] <= '2019-01-01')
    df = df.loc[mask]
    
    df_byday = df.groupby(['date'])['price'].agg([np.mean])
    
    if i == 0:
        df_ = df_byday.reset_index()
        df_ = df_.rename(columns = {'mean':m})
    else:
        df_.index = df_byday.index
        df_[m] = df_byday['mean']

f.subplots_adjust(wspace=0.1)
plt.gcf().autofmt_xdate()
plt.legend(loc='best')
plt.show()

# Plot the prices for the Christmas interval
f, axt = plt.subplots(1,1)
# Setting my colour cycler
my_cycler = (cycler(color=colours))
axt.set_prop_cycle(my_cycler)
plt.ylabel('Average Price')
line = axt.plot_date(df_.date, df_[ext_months] , linestyle="-")
# Add legend to the plot and capitalize each month
axt.legend(line, [s.capitalize() for s in ext_months], loc='upper left', title="Extraction date")
plt.show()
