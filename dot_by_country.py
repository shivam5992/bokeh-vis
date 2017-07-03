from bokeh.plotting import figure, show, output_file

factors = []
x = []
data = open('data/country.csv').read().strip().split("\n")
for line in data:
	factors.append(line.split()[0])
	x.append(line.split()[1])



plt = figure(title="Countries from where companies got acquired by Google", tools="resize,hover", y_range=factors, x_range=[0,15],)

plt.segment(0, factors, x, factors, line_width=2, line_color="green", )
plt.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3, )

output_file("categorical1.html", title="categorical.py")

show(plt)



from collections import OrderedDict

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.iris import flowers

# fill a data frame with the data of interest and create a groupby object
df = flowers[["petal_length", "petal_width", "species"]]
xyvalues = g = df.groupby("species")

# drop that groupby object into a dict
pdict = OrderedDict()

for i in g.groups.keys():
    labels = g.get_group(i).columns
    xname = labels[0]
    yname = labels[1]
    x = getattr(g.get_group(i), xname)
    y = getattr(g.get_group(i), yname)
    pdict[i] = zip(x, y)

# any of the following commented are also valid Scatter inputs
#xyvalues = pdict
#xyvalues = pd.DataFrame(xyvalues)
#xyvalues = xyvalues.values()
#xyvalues = np.array(xyvalues.values())

output_file("iris_scatter.html")

TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,previewsave"

scatter = Scatter(xyvalues, tools=TOOLS, ylabel='petal_width')

show(scatter)