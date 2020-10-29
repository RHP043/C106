import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks_of_percentage=[]
    days_present=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_of_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x":marks_of_percentage,"y":days_present}

def findcorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between marks in percentage and days present: ",corelation[0,1])

def setup():
    data_path = "./data/studentMarksVsDaysPresent.csv"
    dataSource = getDataSource(data_path)
    findcorelation(dataSource)

setup()