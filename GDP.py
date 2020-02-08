import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
import traceback


#Open CSV files GDP.csv and Unemployment.csv and identify the data points
gdp_data = pd.read_csv('GDP.csv')
unemployed = pd.read_csv('Unemployment.csv')

def variable_array(variable):
    """convert selected variable to an array for statistics and graphing purposes"""
    return np.squeeze(np.array(variable))

#call varialbe_array with the three variables to be assessed
x = variable_array(gdp_data[['date']])
gdp = variable_array(gdp_data[['change-current']])
unemployment = variable_array(unemployed[['unemployment']])

#line of best fit
best_fit_line = (gdp+unemployment)/2

#Stats for GDP and Unemployment
covariance = np.cov(gdp, unemployment, bias=True)[0][1]
correlation = np.corrcoef(gdp, unemployment)[0, 1]
print('Statistics of GDP Over Unemployment ')
print('Cost vs. Covariance: ' + str(covariance))
print('Cost vs. Correlation: ' + str(correlation))

#CREATE GDP AND UNEMPLOYMENT LINE GRAPHS
title='GDP Change vs. Unemployment'
file_name= 'GDPvsUnemployment.html'
p = figure(title=title, x_axis_label='Year', y_axis_label='%', plot_width=1000,
toolbar_location="left", tools="pan,reset,save,wheel_zoom")
p.line(x, gdp, color="red", line_width=2, legend_label=" % GDP Change ")
p.line(x, unemployment, color='blue', line_width=2, legend_label="% Unemployed")
p.line(x, best_fit_line, color='gray', line_dash='dashed', line_width=1, legend_label="Fit Line")
p.title.align = 'center'

try:
    show(p)
    print('Open browser to view chart')
except Exception:
    traceback.print_exc()