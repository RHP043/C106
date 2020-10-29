import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv=[]
    average_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))

    return {"x":size_of_tv,"y":average_time_spent}

def findcorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between size of tv and average time spent watching TV is: ",corelation[0,1])

def setup():
    data_path = "./data/sizeofTV.csv"
    dataSource = getDataSource(data_path)
    findcorelation(dataSource)

setup()