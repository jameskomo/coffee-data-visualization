# -*- coding: utf-8 -*-

from plotly.offline import plot  
import plotly.graph_objects as go  
import pandas as pd  

##  The data can not be read from the given Link, since it is a 'Drive' Link
##  Therefore, the data is copied and saved as an URL in web, using the website 'myjson.com'
##  The URL created is accessible on the web through https://api.myjson.com/bins/17ossf

df = pd.read_json("https://api.myjson.com/bins/17ossf.json")  

fig = go.Figure()  

x_plot = []  ##  Arranging the x axis data to be shown on the plot
for i in range(len(df[0])):
    x_plot.append(df[0][i])
    x_plot.append(df[1][i])

print(x_plot)

y_plot = [df[2][0]]  ##  Arranging the y axis data to be shown on the plot
for i in range(len(df[2])):
    y_plot.append(df[2][i])
    y_plot.append(df[2][i])
    

trace1=[(go.Scatter(x=list(x_plot),y=list(y_plot),mode='lines',
    opacity=0.7,text='(Date, Production Qty)',textposition='bottom center'))]
##  The data for the line is inserted. Then, the line is modified.

fig = {'data': trace1,'layout': go.Layout(annotations=[
            go.layout.Annotation(
                text='Data: USDA PS&D',
                align='right',
                showarrow=False,
                xref='paper',
                yref='paper',
                x=1,
                y=0
            )
        ],
            colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
            height=600,title=f"World Coffee Production",
            xaxis={'rangeslider': {'visible': True}, 'type': 'date'},yaxis={"title":"Quantity in tonnes"})}
##  Figure itself is modified. Rangeslider has been added.

# plot(fig)  ##  Plot the constructed figure