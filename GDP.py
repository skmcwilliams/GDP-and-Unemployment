import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
import traceback


#Open CSV files GDP.csv and Unemployment.csv and identify the data points
gdp_data = pd.read_csv('GDP.csv')
unemployed = pd.read_csv('Unemployment.csv')
xvariable=gdp_data[['date']]
x=np.squeeze(np.array(xvariable))
gdpvariable=gdp_data[['change-current']]
gdp=np.squeeze(np.array(gdpvariable))
unemploymentvariable=unemployed[['unemployment']]
unemployment=np.squeeze(np.array(unemploymentvariable))
best_fit_line = (gdp+unemployment)/2

#CREATE GDP AND UNEMPLOYMENT LINE GRAPHS
title='GDP Change vs. Unemployment'
file_name= 'GDPvsUnemployment.html'
p = figure(title=title, x_axis_label='Year', y_axis_label='%', plot_width=1000,
toolbar_location="left", tools="pan,reset,save,wheel_zoom")
p.line(x.squeeze(), gdp.squeeze(), color="red", line_width=2, legend_label=" % GDP Change ")
p.line(x.squeeze(), unemployment.squeeze(), color='blue', line_width=2, legend_label="% Unemployed")
p.line(x.squeeze(), best_fit_line.squeeze(), color='gray', line_dash='dashed', line_width=1, legend_label="Fit Line")
p.title.align = 'center'
output_file(file_name)

#TRYING TO ADD MORE DATA TO SCATTERPLOT - BELOW DATA PRINTS TO TERMINAL
covariance = np.cov(gdp, unemployment, bias=True)[0][1]
correlation = np.corrcoef(gdp, unemployment)[0, 1]
cov = ('Covariance: ' + str(covariance))
cc = ('Correlation: ' + str(correlation))
print(cc)
print(cov)

try:
    show(p)
    print('Open browser to view ' + str(file_name )+ ' chart')
except Exception:
    traceback.print_exc()

