from bokeh.charts import Bar, output_file, show, gridplot
import pandas as pd 
from math import pi
from bokeh.models import (HoverTool, FixedTicker, FuncTickFormatter)


def generate_plot(dataDF):
	html_obj = Bar(config['df'], 'Google company', values='Price', 
			title="Acquired Companies and their Acquision Cost", color=config['color'], 
			xlabel="Acquired Company", ylabel="Amount (in Millions US$)",
			width=1600, height=600, bar_width=0.8, legend = False)
	html_obj.yaxis[0].ticker = FixedTicker(ticks = config['ticks'])
	html_obj.xaxis.major_label_orientation = pi/4
	return html_obj


amountDF = pd.read_csv('data/amount.csv')

config = {
	'df' : amountDF,
	'ticks' : [2000, 4000, 6000, 8000, 10000, 12000],
	'color' : '#f45666'
}
complete = generate_plot(config)

config = {
	'df' : amountDF[3:],
	'ticks' : [100, 500, 1000, 1500, 2000],
	'color' : '#93b1e2'
}
out1 = generate_plot(config)

config = {
	'df' : amountDF[6:],
	'ticks' : [100, 200, 300, 400, 500, 600],
	'color' : '#89c68f'
}
out2 = generate_plot(config)

grid = gridplot([complete, None], [out1, None], [out2, None])
output_file("outputs/bar.html")
show(grid)