import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
import traceback


#Open CSV files GDP.csv and Unemployment.csv and identify the data points
gdp_data = pd.read_csv('GDP.csv')
unemployed = pd.read_csv('Unemployment.csv')
x=gdp_data[['date']]
gdp=gdp_data[['change-current']]
unemployment=unemployed[['unemployment']]
title='Correlation Between US GDP and Unemployment'
file_name= 'GDPvsUnemployment.html'

#MAKE DATA ONE DIMENTIONAL FOR STATISTICAL PURPOSES
gdp_condensed = np.squeeze(np.array(gdp))
unemployment_condensed = np.squeeze(np.array(unemployment))
par = np.polyfit(gdp_condensed, unemployment_condensed,1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in gdp_condensed]

#CREATE GDP AND UNEMPLOYMENT LINE GRAPHS
p = figure(title=title, x_axis_label='year', y_axis_label='%')
p.line(x.squeeze(), gdp.squeeze(), color="red", line_width=2, legend=" GDP ")
p.line(x.squeeze(), unemployment.squeeze(), line_width=2, legend="% unemployed")
output_file(file_name)

#TRYING TO ADD MORE DATA TO SCATTERPLOT - BELOW DATA PRINTS TO TERMINAL
covariance = np.cov(gdp_condensed, unemployment_condensed, bias=True)[0][1]
correlation = np.corrcoef(gdp_condensed, unemployment_condensed)[0, 1]
cov = ('Covariance: ' + str(covariance))
cc = ('Correlation: ' + str(correlation))
print(cc)
print(cov)

try:
    show(p)
    print('Open browser to view ' + str(file_name )+ ' chart')
except Exception:
    traceback.print_exc()

    


