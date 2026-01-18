
####
#
# This shows how to use Python to read a datafile on comma separated value format and process it
# The solution to exercise 1 can be built with this as a start.
# To make the csv file, use the SaveAs function in Excel and save the file on comma separated values format.
# Here I use pandas to handle the data. This is very convenient.
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dataform
import pandas as pd



# Read a data file containing discharge data, one year pr. column.
# I have used a comma separated text file, made by using "Save As" and comma separated in Excel.
# I use pandas in Python to store data, this makes processing the data simpler.
#

data = pd.read_csv('sagelva.csv',sep=",")
print(data.head())
# Make sure that the first column is of type "datetime", the format statement tells how to read the date.
#
data['Dato'] = pd.to_datetime(data['Dato'],format="%Y-%m-%d", errors='coerce')

# Print data on the screen to see that all is ok. Print also the data type to see that they are correct.
# Remove "#" to print
#
print(data)
print(data.dtypes)

# We can plot the data to see what we have read.
# Here the pandas plot
#
#ax = data.plot(x="Dato",kind='line',grid=True,legend=False,linewidth=0.5)
#plt.xlabel("Date")
#plt.ylabel("Discharge (m3/s)")
#ax.xaxis.set_major_formatter(dataform.DateFormatter("%d-%m"))
#plt.show()
#plt.savefig('discharge.png',dpi=200)

######################################
# Compute the mean value for each year and plot them as a bar graph. Here I use matplotlib
# the means are stored in the dataframe aarmid. I added a index column of years and converted this to integer
#
aarmid = pd.DataFrame(data.mean(numeric_only=True),columns = ['MeanQ'])
aarmid = aarmid.reset_index()
aarmid[['index']] = aarmid[['index']].apply(pd.to_numeric)
average=aarmid['MeanQ'].mean()
runoff=average*365*24*3600/1e6
print('Average discharge (m3/s):',average.round(3))
print('Runoff (Mm3):',runoff.round(3))
print(aarmid.round(3))

########## Plot the mean values ##########
plt.bar(aarmid['index'], aarmid['MeanQ'], color='blue', alpha=0.7)
plt.axhline(y=average, color='r', linestyle='--', label=f'Average: {average:.2f} m³/s')

# Add trendline to mean annual discharge
z = np.polyfit(aarmid['index'], aarmid['MeanQ'], 1)  # Linear fit
p = np.poly1d(z)
plt.plot(aarmid['index'], p(aarmid['index']), color='black', linestyle='-', linewidth=2, label='Trendline')
slope = z[0]
intercept = z[1]
eq_text = f"y = {slope:.3f}x + {intercept:.3f}"
plt.text(
    0.05, 0.95, eq_text,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
)
plt.xlabel('Year')
plt.ylabel('Mean Discharge (m³/s)')
plt.title('Mean Annual Discharge')
plt.legend()
plt.grid(axis='y')
plt.savefig('mean_annual_discharge.png', dpi=200)
plt.show()
               
##########to find medians   ##########
aarmedian = pd.DataFrame(data.median(axis=1, numeric_only=True),columns = ['MedianQ'])
aarmedian = aarmedian.reset_index()
aarmedian[['index']] = aarmedian[['index']].apply(pd.to_numeric)
print(aarmedian.round(3))

##########to find 25th and 75th percentiles   ##########
aarpercentile = pd.DataFrame(data.iloc[:, 1:].apply(lambda row: np.percentile(row, 25), axis=1), columns=['25th Percentile'])
aarpercentile75 = pd.DataFrame(data.iloc[:, 1:].apply(lambda row: np.percentile(row, 75), axis=1), columns=['75th Percentile'])
aarpercentile = aarpercentile.reset_index()
aarpercentile[['index']] = aarpercentile[['index']].apply(pd.to_numeric)
print(aarpercentile.round(3))
aarpercentile75 = aarpercentile75.reset_index()
aarpercentile75[['index']] = aarpercentile75[['index']].apply(pd.to_numeric)
print(aarpercentile75.round(3))  

#find minimum and maximum of each row ##
aarmin = pd.DataFrame(data.min(axis=1, numeric_only=True),columns = ['MinQ'])
aarmin = aarmin.reset_index()
aarmin[['index']] = aarmin[['index']].apply(pd.to_numeric)
print(aarmin.round(3))
aarmax = pd.DataFrame(data.max(axis=1, numeric_only=True),columns = ['MaxQ'])
aarmax = aarmax.reset_index()
aarmax[['index']] = aarmax[['index']].apply(pd.to_numeric)
print(aarmax.round(3))   

# You can now use the dataframes aarmid, aarmedian, aarpercentile and aarpercentile75 to plot or process the data further#
# For example, to plot the median values as a line graph:
plt.figure(figsize=(20,10))
plt.plot(aarmedian['index'], aarmedian['MedianQ'], color='green', label='Median')
plt.plot(aarpercentile['index'], aarpercentile['25th Percentile'], color='blue', label='25th Percentile')
plt.plot(aarpercentile75['index'], aarpercentile75['75th Percentile'], color='orange', label='75th Percentile')
plt.plot(aarmin['index'], aarmin['MinQ'], color='red', linestyle='--', label='Min')
plt.plot(aarmax['index'], aarmax['MaxQ'], color='purple', linestyle='--', label='Max')
plt.xlabel('Index')
plt.ylabel('Discharge (m³/s)')
plt.title('Discharge Statistics Over Time')
plt.legend()
plt.grid()
plt.show()
######################################

#find maximum of each year ##
datamax = pd.DataFrame(data.max(numeric_only=True),columns = ['Maximum'])
datamax = datamax.reset_index()
datamax[['index']] = datamax[['index']].apply(pd.to_numeric)
print(datamax.round(3)) 
plt.plot(datamax['index'], datamax['Maximum'], color='brown', linestyle='-', label='Yearly Maximum')
l = np.polyfit(datamax['index'], datamax['Maximum'], 1)  # Linear fit
m = np.poly1d(l)
slope = l[0]
intercept = l[1]
eq_text = f"y = {slope:.3f}x + {intercept:.3f}"
plt.text(
    0.05, 0.95, eq_text,
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
)
plt.plot(datamax['index'], m(datamax['index']), color='black', linestyle='-', linewidth=2, label='Trendline')
plt.xlabel('Index')
plt.ylabel('Discharge (m³/s)')
plt.title('Yearly Maximum Discharge')
plt.grid()
plt.show()



