"""
python script that generates multivariate graph - 
x-axis, y-axis, color, size, shape

"""

from bokeh.plotting import figure, output_file
from bokeh.plotting import show, ColumnDataSource
from bokeh.models import HoverTool, FixedTicker
import pandas as pd 

## read the data from CSV and create DF
inpDF = pd.read_csv("data/acquisition_dataset.csv")

## Selected colors 
colors = {'Communication' : '#ff003b', 
		  'Search' : '#ed89d7',
		  'Publishing' : '#e0ef9e',
		  'Maps' : '#fff200',
		  'Mobile' : '#55f497',
		  'Misc' : '#515991',
		  'AI' : '#f97000',
		  'Youtube' : '#c76de0',
		  'Security' : '#ea7c38',
		  'Social' : '#e1ea38',
		  'Offers' : '#abe554',
		  'Cloud' : '#40e878' }

## Separate Categories and date Wise Acquisitions
xaxis = []
yaxis = []
size = []
color = []
shape = []
desc1 = []
desc2 = []
desc3 = []
for i,row in inpDF.iterrows():
	vals = list(row)
	date = vals[0]
	
	month = date.split("/")[0]
	year = date.split("/")[2]
	category = vals[4]
	dollar = str(row[6])
	continent = row[-1]

	amt = dollar
	if dollar == "nan":
		dollar = "10000000"
		amt = "Undisclosed"

	dollar = dollar.replace(',',"").replace("$","")
	dollar = int(dollar) * 1.0 / 10000

	# fix custom data points
	if dollar in [165000.0, 310000.0, 320000.0, 1250000.0]:
		dollar = float(dollar)/100 + 96600

	dollar = dollar / 1000

	if dollar < 15:
		dollar += 10

	xaxis.append(year)
	yaxis.append(month)
	shape.append(continent)
	color.append(colors[category])
	size.append(dollar)
	
	descr1 = "Company: " + str(row[2]) + " (" + str(row[3]) + "), Category: " +row[4]
	descr2 = "Acquired Date: " + str(row[1]) + ", Amount: " + amt
	descr3 = "Country: " + str(row[5]) + ", Region: " + str(row[-1])
	desc1.append(descr1)
	desc2.append(descr2)
	desc3.append(descr3)



hover = HoverTool(tooltips="""<div>
        			<span style="font-size: 14px; font-weight: bold;">@desc1</span> <br>
        			<span style="font-size: 13px;">@desc2</span> <br>
        			<span style="font-size: 12px;">@desc3</span><br>
        			</div>""")

output_file("outputs/multivariate.html")
p = figure(plot_width=1500, plot_height=900, tools=[hover], title="Google Acquisitions over time")

shapes = {}
for i, each in enumerate(shape):
	if each not in shapes:
		shapes[each] = {'xaxis' : [], 'yaxis' : [], 'size' : [], 'color' : [], 'desc1' : [], 'desc2' : [], 'desc3' : []}

	shapes[each]['xaxis'].append(xaxis[i])
	shapes[each]['yaxis'].append(yaxis[i])
	shapes[each]['color'].append(color[i])
	shapes[each]['size'].append(size[i])
	shapes[each]['desc1'].append(desc1[i])
	shapes[each]['desc2'].append(desc2[i])
	shapes[each]['desc3'].append(desc3[i])

different_shapes = shapes.keys()
for shape, value in shapes.iteritems():
	source = ColumnDataSource(data=dict(x=value['xaxis'], y=value['yaxis'], 
							  color=value['color'], size=value['size'], desc1=value['desc1'],
							  desc2=value['desc2'], desc3=value['desc3']))
	if shape == 'NorthAmerica':
		p.circle('x', 'y', size='size', color='color', alpha=0.2, source=source)
	elif shape == 'SA':
		p.square('x', 'y', size='size', color='color', alpha=2, source=source)
	elif shape == 'Aus':
		p.triangle('x', 'y', size='size', color='color', alpha=2, source=source)
	elif shape == 'Asia':
		p.diamond('x', 'y', size='size', color='color', alpha=2, source=source)
	elif shape == 'Euo':
		p.cross('x', 'y', size='size', color='color', alpha=2, source=source)
	
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.yaxis[0].ticker = FixedTicker(ticks = [1,2,3,4,5,6,7,8,9,10,11,12])
p.xaxis[0].ticker = FixedTicker(ticks = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012, 2013,2014,2015,2016,2017])
show(p)