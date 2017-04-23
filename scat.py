from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], [2011, 7, 2, 4, 5], size=[1,3,6,80,23], color=["navy",'green','blue', 'red','black'], alpha=0.5)

# show the results
show(p)