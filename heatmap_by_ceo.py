import pandas as pd 
import csv 

from bokeh.charts import HeatMap, output_file, show
from bokeh.models import HoverTool
from bokeh.models import FixedTicker
from bokeh.palettes import Oranges9, Oranges9
from bokeh.models import FuncTickFormatter

def dataset_preparation(row_data, upper_y):
	dataset = []
	input_data = list(reversed(row_data))

	chunks = [input_data[i:i + 20] for i in xrange(0, len(input_data), 20)]
	
	for yindex, chunk in enumerate(chunks):
		for index, each in enumerate(chunk):
			each.append(index + 1)
			each.append(upper_y - yindex)
			each.append(5)

			dataset.append(each)

	return dataset

def ceo_ticker():
	if tick == "23":
		return "Sundar Pichai (2015 - Present)"
	elif tick == "16":
		return "Larry Page (2011 - 2015)"
	elif tick == "11":
		return "Eric Shmidt (2011 - 2011)"

with open('data/google_derived_data.csv') as fin:
	reader = csv.reader(fin)

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

		# Categorize CEOs
		if int(year) >= 2015:
			ceo3.append(row)
		elif int(year) >= 2011:
			ceo2.append(row)
		else:
			ceo1.append(row)

	ceo_dataset1 = dataset_preparation(ceo1, 25)
	ceo_dataset2 = dataset_preparation(ceo2, 18)
	ceo_dataset3 = dataset_preparation(ceo3, 11)
	
	by_ceo = []
	by_ceo.extend(ceo_dataset1)
	by_ceo.extend(ceo_dataset2)
	by_ceo.extend(ceo_dataset3)

	header.append('x')
	header.append('y')
	header.append('count')
	ceoDF = pd.DataFrame(by_ceo, columns = header)
	
	year_hover = HoverTool(tooltips=[("Company:", "@Google_company")])    
	html_object = HeatMap(ceoDF, x='x', y='y', values='count', stat=None, width=800, height=600, 
												legend=False, palette=Oranges9, tools = [year_hover])
	 
	html_object.xaxis[0].ticker = FixedTicker(ticks=[25])
	html_object.yaxis[0].ticker = FixedTicker(ticks=[23,16,11])

	html_object.xaxis.axis_label = ""
	html_object.yaxis.axis_label = ""

	html_object.xaxis.axis_line_width = 0
	html_object.yaxis.axis_line_width = 0

	html_object.xaxis.visible = False


	html_object.outline_line_width = 0
	html_object.outline_line_color = "white"
	html_object.min_border_top = 80
	html_object.yaxis.major_label_text_color = "black"


	html_object.yaxis.formatter = FuncTickFormatter.from_py_func(ceo_ticker)	

	output_file("heatmap_ceo.html", title="")
	show(html_object)