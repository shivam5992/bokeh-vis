from bokeh.plotting import figure, show, output_file
import pandas as pd 
import numpy as np

def formatted_date(date):
	dat = date.split("/")[1]
	if int(dat) < 10:
		dat = "0" + dat

	mn = date.split("/")[0]
	if int(mn) < 10:
		mn = "0" + mn

	return date.split("/")[2] + "-" + mn + "-" + dat

def datetime(x):
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

	# real_dates = sorted(real)
	# for i, key in enumerate(real_dates):
	# 	try:
	# 		print key - real_dates[i+1]
	# 	except Exception as E:
	# 		continue

	times = datetime(times)
	return times, values



inpDF = pd.read_csv('data/google_derived_data.csv')
inpDF['date'] = inpDF['Acquisition_date'].apply(lambda x : formatted_date(x))
dates = list(inpDF['date'])

dates, acquisitions = aggregate_date(dates)

html_object = figure(x_axis_type="datetime", title="Number of acquisitions - Timeseries", width=1200, height=500)
html_object.grid.grid_line_alpha = 0
html_object.xaxis.axis_label = 'Date'
html_object.yaxis.axis_label = '# acquisitions'
html_object.ygrid.band_fill_alpha = 0.1

html_object.circle(dates, acquisitions, size=14, alpha=0.2, color='navy')
html_object.circle(aapl_dates, aapl, size=4, legend='close', color='darkgrey', alpha=0.2)

output_file("stocks.html", title="Number of acquisitions - Timeseries")
show(html_object)