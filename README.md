Discharge Data Analysis with Python

This repository contains a Python script for reading, processing, and analyzing river discharge data stored in a comma-separated values (CSV) file. The analysis focuses on annual discharge statistics and basic trend analysis, with visualizations produced using Matplotlib.

The code is suitable for hydrology, environmental science, or engineering coursework involving time-series data.

Features

1. Reads discharge data from a CSV file exported from Excel

2. Converts date columns to proper datetime format

3. Computes annual statistics:

-Mean discharge

-Median discharge

-Minimum and maximum discharge

-25th and 75th percentiles

-Annual maximum discharge

4. Calculates long-term average discharge and total runoff volume

5. Produces publication-ready plots:

-Mean annual discharge (bar plot with trendline)

-Statistical time series (median, percentiles, min/max)

-Annual maximum discharge with linear trend



Requirements

The script uses standard scientific Python libraries:

Python 3.x

NumPy

Pandas

Matplotlib
