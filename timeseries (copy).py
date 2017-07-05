from bokeh.plotting import figure, show, output_file
import pandas as pd 
import numpy as np
from datetime import datetime

def formatted_date(date):
	dat = date.split("/")[1]
	if int(dat) < 10:
		dat = "0" + dat

	mn = date.split("/")[0]
	if int(mn) < 10:
		mn = "0" + mn

	return date.split("/")[2] + "-" + mn + "-" + dat

def np_datetime(x):
    return np.array(x, dtype=np.datetime64)

def aggregate_date(dates):
	aggregated = {}
	real = {}
	for date in dates:
		ymd = date.split("-")
		ym = ymd[0] + ymd[1]
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
			
		except Exception as E:
			continue


	times = np_datetime(times)
	time_differences = np_datetime(time_differences)


	return times, values, time_differences, differences



inpDF = pd.read_csv('data/google_derived_data.csv')
inpDF['date'] = inpDF['Acquisition_date'].apply(lambda x : formatted_date(x))
dates = list(inpDF['date'])

dates, acquisitions, times, differences = aggregate_date(dates)

html_object = figure(x_axis_type="datetime", title="Number of acquisitions - Timeseries", width=1200, height=500)
html_object.grid.grid_line_alpha = 0
html_object.xaxis.axis_label = 'Date'
html_object.yaxis.axis_label = '# acquisitions'
html_object.ygrid.band_fill_alpha = 0.1

html_object.circle(dates, acquisitions, size=16, alpha=0.2, legend="# acquisitions", color='navy')
# html_object.line(times, differences, color='darkgrey', legend="Average Gap bw acquisitions", alpha=0.8)

output_file("timeseries.html", title="Number of acquisitions - Timeseries")
show(html_object)