import pandas as pd
import csv
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


unemployed = pd.read_csv('Unemployment.csv')
high = unemployed[unemployed['unemployment'] > 8.5]
print(high)
