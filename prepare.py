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


with open('data/google_derived_data.csv') as fin:
	reader = csv.reader(fin)

	category4 = []
	category3 = []
	category2 = []
	category1 = [] 
	category0 = []

	i = 0
	for row in reader:
		i += 1 
		if i == 1:
			header = row 
			continue 

		year = row[1]
		if int(year) < 2004:
			category0.append(row) 
		elif int(year) < 2008:
			category1.append(row) 
		elif int(year) < 2012:
			category2.append(row) 
		elif int(year) < 2016:
			category3.append(row) 
		elif int(year) < 2018:
			category4.append(row)

		
		
	dataset1 = dataset_preparation(category4, 25)
	dataset2 = dataset_preparation(category3, 19)
	dataset3 = dataset_preparation(category2, 14)
	dataset4 = dataset_preparation(category1, 10)
	dataset5 = dataset_preparation(category0, 7)
	
	rows = []
	rows.extend(dataset1)
	rows.extend(dataset2)
	rows.extend(dataset3)
	rows.extend(dataset4)
	rows.extend(dataset5)

	header.append('x')
	header.append('y')
	header.append('count')
	inpDF = pd.DataFrame(rows, columns = header)
	
	html_object = HeatMap(inpDF, x='x', y='y', values='count', stat=None, width=800, height=600, legend=False, palette=YlGn9)
	
	html_object.xaxis[0].ticker = FixedTicker(ticks=[25])
	html_object.yaxis[0].ticker = FixedTicker(ticks=[22,19,13,8,4])

	html_object.xaxis.axis_label = ""
	html_object.yaxis.axis_label = ""

	html_object.xaxis.axis_line_width = 1
	html_object.yaxis.axis_line_width = 1

	def ticker():
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

	html_object.yaxis.formatter = FuncTickFormatter.from_py_func(ticker)	

	output_file("heatmap.html", title="Year Wise Category wise Number of Google Acquisitions")
	show(html_object)