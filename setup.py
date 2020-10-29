import plotly.express as px
import csv
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature",y="Ice-cream Sales")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales=[]
    cold_drink_sales=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))

    return {"x":ice_cream_sales,"y":cold_drink_sales}

def findcorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between temperature and ice cream sales is: ",corelation[0,1])

def setup():
    data_path = "./data/icecreamVsColdDrink.csv"
    dataSource = getDataSource(data_path)
    findcorelation(dataSource)
    plotfigure(data_path)

setup()