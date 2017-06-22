from bokeh.charts import Bar, output_file, show
import pandas as pd 

amountDF = pd.read_csv('data/amount.csv')
amountDF = amountDF[3:]

p = Bar(amountDF, 'Google company', values='Price', title="Total Amount by company", color="wheat", width=1500, height=1000)

output_file("bar.html")

show(p)