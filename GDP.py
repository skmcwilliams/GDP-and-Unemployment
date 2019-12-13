import pandas as pd
from bokeh.plotting import figure, output_file, save

gdp = pd.read_csv('GDP.csv')
unemployed = pd.read_csv('Unemployment.csv')
x=gdp[['date']]
gdp_change=gdp[['change-current']]
unemployment=unemployed[['unemployment']]
title='Correlation Between US GDP and Unemployment'
file_name="GDP.html"

p = figure(title=title, x_axis_label='year', y_axis_label='%')
p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
output_file(file_name)
save(p)
    


