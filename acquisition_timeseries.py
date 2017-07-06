"""
python script that generates timeseries plot - line and circle
using bokeh library.

line : gap between the two dates
circle : repersenting every node and its count
"""

from bokeh.plotting import figure, show, output_file
from datetime import datetime
import pandas as pd 
import numpy as np


# Utility function to format date
def formatted_date(date):
	year = date.split("/")[2]

	day = date.split("/")[1]
	day = "0"+day if int(day)<10 else day

	month = date.split("/")[0]
	month = "0"+month if int(month)<10 else month
	
	reformed_data = year + "-" + month + "-" + day
	return reformed_data


# Utility function to convert a list of dates into np array of dates
def np_datetime(x):
    return np.array(x, dtype=np.datetime64)


# Function to aggregate datapoints on the basis of dates
def aggregate_date(dates):
	aggregated = {}
	real = {}
	for date in dates:
		ymd = date.split("-")
		padded = ymd[0] + "-" + ymd[1] + "-" + "01"

		if padded not in aggregated:
			aggregated[padded] = 1 
		aggregated[padded] += 1 

		if date not in real:
			real[date] = 1 
		real[date] += 1 

	times = []
	values = []
	for key in sorted(aggregated.keys()):
		times.append(key)
		values.append(aggregated[key])

	# code to compute time gap between two dats
	time_differences = []
	differences = []
	real_dates = sorted(real)
	for i, key in enumerate(real_dates):
		try:
			d1 = datetime.strptime(key, '%Y-%m-%d')
			d2 = datetime.strptime(real_dates[i+1], '%Y-%m-%d')

			time_differences.append(key)
			difference = str(d2 - d1).split(",")[0].split()[0]
			differences.append( difference )
		except:
			continue

	times = np_datetime(times)
	time_differences = np_datetime(time_differences)

	return times, values, time_differences, differences

# Function to generate time series plot
def generate_plot(line = False):
	inpDF = pd.read_csv('data/acquisition_dataset.csv')

	inpDF['date'] = inpDF['Acquisition_date'].apply(lambda x : formatted_date(x))
	dates = list(inpDF['date'])

	dates, acquisitions, times, differences = aggregate_date(dates)

	# create bokeh html plot
	html_object = figure(x_axis_type="datetime", title="Number of acquisitions - Timeseries", width=1200, height=500)
	html_object.grid.grid_line_alpha = 0
	html_object.xaxis.axis_label = 'Date'
	html_object.yaxis.axis_label = '# acquisitions'
	html_object.ygrid.band_fill_alpha = 0.1

	html_object.circle(dates, acquisitions, size=16, alpha=0.2, legend="# acquisitions", color='navy')
	if line:
		html_object.line(times, differences, color='darkgrey', legend="Average Gap bw acquisitions", alpha=0.8)

	output_file("outputs/gap_timeseries.html", title="Number of acquisitions - Timeseries")


if __name__ == '__main__':
	generate_plot(line = True)