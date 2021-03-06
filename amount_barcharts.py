"""
python script that generates bar charts for a dataframe

"""

from bokeh.charts import Bar, output_file, show, gridplot
from bokeh.models import HoverTool, FixedTicker
import pandas as pd 
from math import pi

# Function to generate bar chart with respect to data provided
def generate_plot(config):
	html_obj = Bar(config['df'], 'Google company', values='Price', 
								title="Acquired Companies and their Acquision Cost", 
								color=config['color'], 
								xlabel="Acquired Company", 
								ylabel="Amount (in Millions US$)",
								width=1600, 
								height=600, 
								bar_width=0.8, 
								legend = False)

	html_obj.yaxis[0].ticker = FixedTicker(ticks = config['ticks'])
	html_obj.xaxis.major_label_orientation = pi/4

	output_file("outputs/bar"+config['name']+".html")
	return html_obj

if __name__ == '__main__':
	amountDF = pd.read_csv('data/acquisition_amount.csv')

	config = {
		'df' : amountDF,
		'ticks' : [2000, 4000, 6000, 8000, 10000, 12000],
		'color' : '#f45666',
		'name' : 'level1'
	}
	complete = generate_plot(config)

	config = {
		'df' : amountDF[3:],
		'ticks' : [100, 500, 1000, 1500, 2000],
		'color' : '#93b1e2',
		'name' : 'level2'
	}
	out1 = generate_plot(config)

	config = {
		'df' : amountDF[6:],
		'ticks' : [100, 200, 300, 400, 500, 600],
		'color' : '#89c68f',
		'name' : 'level3'
	}
	out2 = generate_plot(config)