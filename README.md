The GDP Python program will pull the annual GDP from one CSV file and Unemployment from the other CSV file. This will then be plotted using bokeh and show the file in an html file tilted "GDPvsUnemployment.html" that will open in your browser

This program:
- Reads data from both CSV files and cleans it to make it more readable for Python
- Plots the data from the two CSV files to compare GDP change to unemployment from 1948 to 2016
- Weights each variable the same and creates a fit line, tracking the overall trend throughout the time frame
