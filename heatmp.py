from bokeh.charts import HeatMap, output_file, show
import pandas as pd

ycc = pd.read_csv('data/year_category_count.csv')
html_object = HeatMap(ycc, x='Year', y='Category', values='Count', stat=None, sort_dim={'x': False}, width=1000)

output_file("heatmap.html", title="Year Wise Category wise Number of Google Acquisitions")
show(html_object)