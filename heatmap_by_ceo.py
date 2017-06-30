from bokeh.models import (HoverTool, FixedTicker, FuncTickFormatter, ColumnDataSource)
from bokeh.charts import HeatMap, output_file, show
from bokeh.palettes import Oranges9, Oranges9

import pandas as pd 
import csv 

from configs import ceo, year

def dataset_preparation(row_data, upper_y, chunk_len = 20, max_color = 5):
	input_data = list(reversed(row_data))
	chunks = [input_data[i:i + chunk_len] for i in xrange(0, len(input_data), chunk_len)]

	dataset = []
	for y_index, chunk in enumerate(chunks):
		for x_index, row in enumerate(chunk):
			updated_row = row 
			
			x_coordinate = x_index + 1 
			updated_row.append(x_coordinate)
			
			y_coordinate = upper_y - y_index 
			updated_row.append(y_coordinate)
			
			z_coordinate = max_color - y_index
			updated_row.append(z_coordinate)

			dataset.append(updated_row)
	return dataset


def beautify_heatmap(html_object, ticks, ticker_func):
	html_object.yaxis[0].ticker = FixedTicker(ticks = ticks)

	html_object.xaxis.axis_label = ""
	html_object.yaxis.axis_label = ""
	html_object.xaxis.visible = False

	html_object.outline_line_width = 0
	html_object.outline_line_color = "white"
	html_object.yaxis.major_label_text_color = "black"

	html_object.yaxis.formatter = FuncTickFormatter.from_py_func(ticker_func)	
	return html_object

def read_dataset(chart_config):
	data_config = chart_config['data_config']

	with open('data/google_derived_data.csv') as fin:
		index = 0 

		reader = csv.reader(fin)
		for row in reader:
			index += 1 

			if index == 1:
				header = row 
				header.extend(['x', 'y', 'count'])
				continue 

			year = int(row[1])

			# Improve this !!!!!!!!!!!!!!!!!!!!!!!!!!

			if len(data_config) == 3:
				if year >= data_config[2]['starting_year']:
					data_config[2]['dataset'].append(row)
				elif year >= data_config[1]['starting_year']:
					data_config[1]['dataset'].append(row)
				else:
					data_config[0]['dataset'].append(row)

			elif len(data_config) == 4:
				if year >= data_config[3]['starting_year']:
					data_config[3]['dataset'].append(row)
				elif year >= data_config[2]['starting_year']:
					data_config[2]['dataset'].append(row)
				elif year >= data_config[1]['starting_year']:
					data_config[1]['dataset'].append(row)
				else:
					data_config[0]['dataset'].append(row)

			elif len(data_config) == 5:
				if year >= data_config[4]['starting_year']:
					data_config[4]['dataset'].append(row)
				elif year >= data_config[3]['starting_year']:
					data_config[3]['dataset'].append(row)
				elif year >= data_config[2]['starting_year']:
					data_config[2]['dataset'].append(row)
				elif year >= data_config[1]['starting_year']:
					data_config[1]['dataset'].append(row)
				else:
					data_config[0]['dataset'].append(row)

	chart_config['data_config'] = data_config
	chart_config['header'] = header
	return chart_config

def prepare_heatmap(chart_config):
	data_config = chart_config['data_config']
	ticks = chart_config['ticks']
	ticker_func = chart_config['ticker_func']

	by_category = []
	for i in range(len(data_config)):
		data_config[i]['dataset'] = dataset_preparation(data_config[i]['dataset'], data_config[i]['upper_index'])
		by_category.extend(data_config[i]['dataset'])

	inpDF = pd.DataFrame(by_category, columns = chart_config['header'])

	# Not Working  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	hover_object = HoverTool(tooltips="""<div><span style="font-size: 17px;">@company</span></div>""")
	html_object = HeatMap(inpDF, x='x', y='y', values='count',
							     stat=None, width=1000, height=600, 
								 legend=False, palette=Oranges9, tools=[hover_object],
								 title=chart_config['chart_title'], toolbar_location="above")
 
	html_object = beautify_heatmap(html_object, ticks, ticker_func)
	output_file("outputs/heatmap_" + chart_config['category'] + ".html", title=chart_config['chart_title'])
	show(html_object)

if __name__ == '__main__':
	chart_config = read_dataset(ceo)
	prepare_heatmap(chart_config)