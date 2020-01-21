import pandas as pd
import numpy as np
from bokeh.models import Slope, Label
from bokeh.plotting import figure, output_file, show
from sklearn.linear_model import LinearRegression
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

"""#MAKE DATA ONE DIMENTIONAL FOR STATISTICAL PURPOSES
par = np.polyfit(x, unemployment,1, full=True)
slope=par[0][0]
intercept=par[0][1]
unemploymentpredicted = [slope*i + intercept  for i in gdp]
"""

#CREATE GDP AND UNEMPLOYMENT LINE GRAPHS
title='GDP Change vs. Unemployment Change'
file_name= 'GDPvsUnemployment.html'
p = figure(title=title, x_axis_label='year', y_axis_label='%')
p.line(x.squeeze(), gdp.squeeze(), color="red", line_width=2, legend_label=" % GDP Change ")
p.line(x.squeeze(), unemployment.squeeze(), color='blue', line_width=2, legend_label="% Unemployed")
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

    


