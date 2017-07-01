from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.charts import HeatMap, output_file, show
import pandas as pd

output_file("slider.html")

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")

p2 = figure(plot_width=300, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")


dataframe = pd.read_csv('data/year_category_count.csv')

html_object = HeatMap(dataframe, x='Year', y='Category', values='Count', stat=None, sort_dim={'x': False}, width=1000)
tab3 = Panel(child=html_object, title="heatmap")

tabs = Tabs(tabs=[ tab1, tab2, tab3 ])

show(tabs)