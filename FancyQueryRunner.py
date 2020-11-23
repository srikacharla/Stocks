import pandas as pd
import numpy as np
from os import walk


columnOptions = ["Open", "High", "Low", "Close", "Adj", "Close", "Volume"]
fileNames = []
columnIndex = 0


def getInputAndOpenFile():
    fileName = input("Please enter the file name that you want to open")
    return pd.read_csv(f"DataSets/US/{fileName}.csv"), fileName


def getColumnInputAndPrintIt(file):
    print("Please enter the column that you want to compare the companies with. The below are your options:")
    for x in range(len(columnOptions)):
        print(x + 1, columnOptions[x])
    index = int(input())
    global columnIndex
    columnIndex = index
    column = file.get([columnOptions[index - 1], "Date"])
    return column


numberOfCompanies = int(input("Please enter the number of companies that you want to compare"))
columns = []
for i in range(0, numberOfCompanies):
    file, fileName = getInputAndOpenFile()
    fileNames.append(fileName)
    columns.append(getColumnInputAndPrintIt(file))

datesToConsider = 0
if columns[0].get("Date").get(0) < columns[1].get("Date").get(0):
    datesToConsider = 0
else:
    datesToConsider = 1
finalDates = columns[datesToConsider].get("Date")
olderCompanyColumn = columns[datesToConsider].get(columnOptions[columnIndex - 1])
differenceInLength = len(columns[datesToConsider].get(columnOptions[columnIndex - 1])) - len(
    columns[datesToConsider - 1].get(columnOptions[columnIndex - 1]))
newerCompanyColumn = ([0] * differenceInLength) + list(columns[datesToConsider - 1].get(columnOptions[columnIndex - 1]))

dict = {'Date': finalDates, fileNames[datesToConsider]: olderCompanyColumn, fileNames[datesToConsider-1]: newerCompanyColumn}

df = pd.DataFrame(dict)
df.to_csv('NewFile.csv')

# finalDates = columns[0].get("Date")> columns[1].get("Date") if columns[1].get("Date") else columns[0].get("Date")
# print(finalDates)
