from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
import pandas as pd 

## read the data from CSV and create DF
inpDF = pd.read_csv("derived_data.csv")

## Separate Categories and Year Wise Acquisitions
categories = []
year_wise = {}
for i,row in inpDF.iterrows():
	vals = list(row)
	year = vals[1]
	category = vals[4]

	if year not in year_wise:
		year_wise[year] = {}

	if category not in year_wise[year]:
		year_wise[year][category] = 0

	year_wise[year][category] += 1
	if category not in categories:
		categories.append(category)

## Selected colors 
colors = {'Communication' : '#5d95ef', 
		  'Search' : '#ed89d7',
		  'Publishing' : '#e0ef9e',
		  'Maps' : '#f27f52',
		  'Mobile' : '#55f497',
		  'Misc' : '#515991',
		  'AI' : '#efec8f',
		  'Youtube' : '#c76de0',
		  'Security' : '#ea7c38',
		  'Social' : '#e1ea38',
		  'Offers' : '#abe554',
		  'Cloud' : '#40e878' }

## Create data for bokeh plot
x_axis = year_wise.keys()
x_axis = sorted(x_axis)

pairs = []
for year in sorted(year_wise):
	values = year_wise[year]
	for category, count in values.iteritems():
	 	pairs.append((year, count, category))

xtab = [int(pair[0])+float(i%3)/10 for i,pair in enumerate(pairs)]
year = [pair[0] for pair in pairs]
ytab = [pair[1] for pair in pairs]
stab = [size*8 for size in ytab]
ctab = [colors[pair[2]] for pair in pairs]
desc = [pair[2] for pair in pairs]

## Generate Plot
source = ColumnDataSource(data=dict( x=xtab, y=ytab, year=year, color=ctab, size=stab, desc=desc))

hover = HoverTool(tooltips="""<div>
        			<span style="font-size: 17px; font-weight: bold;">@desc</span> <br>
					<span style="font-size: 14px; font-weight: bold;">Companies: @y, year: @year</span>
        			</div>""")

output_file("google.html")

p = figure(plot_width=1500, plot_height=900, tools=[hover], title="Google Acquisitions over time")
p.circle('x', 'y', size='size', color='color', alpha=0.5, source=source)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

show(p)

# fix scatter 
# create heat map - year wise category wise counts
# plot $ amounts on map 
# time series of all companies 