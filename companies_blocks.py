from bokeh.models import (HoverTool, FixedTicker, FuncTickFormatter, ColumnDataSource)
from bokeh.charts import HeatMap, output_file, show, gridplot
from bokeh.plotting import figure 

import pandas as pd 
import csv 
from math import floor 

from blocks_config import ceo, year, category, compl

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

	html_object.xgrid.grid_line_color = None
	html_object.ygrid.grid_line_color = None

	html_object.yaxis.formatter = FuncTickFormatter.from_py_func(ticker_func)	
	return html_object

def read_dataset(chart_config):
	data_config = chart_config['data_config']

	with open('data/dataset.csv') as fin:
		index = 0 

		reader = csv.reader(fin)
		for row in reader:
			index += 1 

			if index == 1:
				header = row 
				header.extend(['x', 'y', 'count'])
				continue 

			year = int(row[1])
			category = row[4] 


			if chart_config['category'] == 'category':
				for each in data_config:
					if category == each['name']: 
						each['dataset'].append(row)
						break

			elif chart_config['category'] == 'ceo':
				if year >= data_config[2]['starting_year']:
					data_config[2]['dataset'].append(row)
				elif year >= data_config[1]['starting_year']:
					data_config[1]['dataset'].append(row)
				else:
					data_config[0]['dataset'].append(row)

			elif chart_config['category'] == 'year':
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

			elif chart_config['category'] == 'compl':
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
	
	X = inpDF.x.values 
	Y = inpDF.y.values 
	Count = inpDF['count'].values 
	Desc = inpDF.Google_company.values 

	data = {'X':X,'Y':Y,'count':Count, 'desc':Desc, 'date':inpDF['Acquisition_date'].values, 'cat' : inpDF['Category'].values,
				'country' : inpDF['Country'].values, 'amt':inpDF['Price'].values} 

	palette = chart_config['col_ind']
	N, min, max = len(palette), Count.min(), Count.max() 
	data['color'] = [] 
	for x in data['count']: 
		ind = int(floor((x-min)/(max-min)*(N-1)) )

		data['color'].append(palette[4][0]) 
		
	source = ColumnDataSource(data) 
	hover = HoverTool( tooltips=[("Company:", "@desc"), ("Acquired Date:", "@date"), ("Category:", "@cat"),
									("Country:", "@country"), ("Amount:", "@amt")] ) 
	html_object = figure(tools=[hover], width=chart_config['width'], height=chart_config['height'], 
								 title=chart_config['chart_title'], toolbar_location="above") 
	html_object.rect(x='X', y='Y', width=1, height=1, fill_color='color', line_color="white", source=source) 

	html_object = beautify_heatmap(html_object, ticks, ticker_func)
	output_file("outputs/block_" + chart_config['category'] + ".html", title=chart_config['chart_title'])
	show(html_object)
	
if __name__ == '__main__':
	chart_config = read_dataset(compl)
	compl = prepare_heatmap(chart_config)

	chart_config = read_dataset(year)
	yr = prepare_heatmap(chart_config)

	chart_config = read_dataset(ceo)
	co = prepare_heatmap(chart_config)

	chart_config = read_dataset(category)
	cat = prepare_heatmap(chart_config)