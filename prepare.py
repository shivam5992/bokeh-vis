import pandas as pd 
import csv 

from bokeh.charts import HeatMap, output_file, show
from bokeh.models import HoverTool
from bokeh.models import FixedTicker
from bokeh.palettes import YlGn9
from bokeh.models import FuncTickFormatter

def dataset_preparation(row_data, upper_y):
	dataset = []
	input_data = reversed(row_data)

	for i, each in enumerate(input_data): 
		index = i
		if index >= 60:
			each.append(index - 60)
			each.append(upper_y)
			each.append(4)
		elif index >= 40:
			each.append(index - 40)
			each.append(upper_y - 1)
			each.append(3)
		elif index >= 20:
			each.append(index - 20)
			each.append(upper_y - 2)
			each.append(2)
		else:
			each.append(index)
			each.append(upper_y - 3)
			each.append(1)

		dataset.append(each)
	return dataset


def year_ticker():
	if tick == 22:
		return "2016 - Present"
	elif tick == 19:
		return "2012 - 2016"
	elif tick == 13:
		return "2008 - 2012"
	elif tick == 8:
		return "2004 - 2008"
	elif tick == 4:
		return "2000 - 2004"

with open('data/google_derived_data.csv') as fin:
	reader = csv.reader(fin)

	year4 = []
	year3 = []
	year2 = []
	year1 = [] 
	year0 = []

	ceo1 = []
	ceo2 = []
	ceo3 = []

	i = 0
	for row in reader:
		i += 1 
		if i == 1:
			header = row 
			continue 

		year = row[1]

		# Categorize Years
		if int(year) < 2004:
			year0.append(row) 
		elif int(year) < 2008:
			year1.append(row) 
		elif int(year) < 2012:
			year2.append(row) 
		elif int(year) < 2016:
			year3.append(row) 
		elif int(year) < 2018:
			year4.append(row)

		# Categorize CEOs
		if int(year) < 2018:
			ceo3.append(row)
		elif int(year) < 2015:
			ceo2.append(row)
		elif int(year) < 2011:
			ceo1.append(row)


		
	year_dataset1 = dataset_preparation(year4, 25)
	year_dataset2 = dataset_preparation(year3, 19)
	year_dataset3 = dataset_preparation(year2, 14)
	year_dataset4 = dataset_preparation(year1, 10)
	year_dataset5 = dataset_preparation(year0, 7)
	
	by_year = []
	by_year.extend(year_dataset1)
	by_year.extend(year_dataset2)
	by_year.extend(year_dataset3)
	by_year.extend(year_dataset4)
	by_year.extend(year_dataset5)

	header.append('x')
	header.append('y')
	header.append('count')
	yearDF = pd.DataFrame(by_year, columns = header)
	
	year_hover = HoverTool(tooltips=[("Company:", "@Google_company")])    
	html_object = HeatMap(yearDF, x='x', y='y', values='count', stat=None, width=800, height=600, 
												legend=False, palette=YlGn9, tools = [year_hover])
	 
	html_object.xaxis[0].ticker = FixedTicker(ticks=[25])
	html_object.yaxis[0].ticker = FixedTicker(ticks=[22,19,13,8,4])

	html_object.xaxis.axis_label = ""
	html_object.yaxis.axis_label = ""

	html_object.xaxis.axis_line_width = 1
	html_object.yaxis.axis_line_width = 1

	html_object.yaxis.formatter = FuncTickFormatter.from_py_func(year_ticker)	

	output_file("heatmap.html", title="Year Wise Category wise Number of Google Acquisitions")
	show(html_object)