from bokeh.plotting import figure, show, output_file

factors = []
x = []
data = open('data/country.csv').read().strip().split("\n")
for line in data:
	factors.append(line.split()[0])
	x.append(line.split()[1])

p1 = figure(title="Countries from where companies got acquired by Google", tools="resize,hover", y_range=factors, x_range=[0,160],)

p1.segment(0, factors, x, factors, line_width=2, line_color="green", )
p1.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3, )

output_file("categorical.html", title="categorical.py")

show(p1)



p2 = figure(title="Countries from where companies got acquired by Google", tools="resize,hover", y_range=factors, x_range=[0,15],)

p2.segment(0, factors, x, factors, line_width=2, line_color="green", )
p2.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3, )

output_file("categorical1.html", title="categorical.py")

show(p2)

