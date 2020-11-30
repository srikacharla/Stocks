from os import walk
import pandas as pd
import numpy as np
import math

f = []
files = []

for (dirpath, dirnames, filenames) in walk(f"DataSets/IndiaFinalFinal"):
    f.extend(filenames)
    break
print(f)
for name in f:
    files.append(pd.read_csv(f"DataSets/IndiaFinalFinal/{name}"))

profitsDict = {}
totalIntradayProfitOfAllCompanies = list()
totalInvestingProfitOfAllCompanies = list()
for i in range(0, len(files)):
    columns = files[i].get(["Date", "Open", "Close"])
    datesAsNumpy = columns.Date.array.to_numpy()
    index = np.where(datesAsNumpy == "2019-09-25")
    closeAsNumpy = columns.Close.array.to_numpy()
    openAsNumpy = columns.Open.array.to_numpy()
    startingCloseValue = closeAsNumpy[index]
    endingCloseValue = closeAsNumpy[-1]
    startingToClosingCloseValues = closeAsNumpy[index[0].tolist()[0]:-1]
    startingToClosingOpenValues = openAsNumpy[index[0].tolist()[0]:-1]
    totalIntradayProfit = 0
    for index1 in range(0, len(startingToClosingCloseValues)):
        if not math.isnan(startingToClosingOpenValues[index1]) and not math.isnan(startingToClosingCloseValues[index1]):
            totalIntradayProfit += (startingToClosingCloseValues[index1] - startingToClosingOpenValues[index1])
    totalIntradayProfitOfAllCompanies.append(totalIntradayProfit)
    totalInvestingProfitOfAllCompanies.append(endingCloseValue - startingCloseValue[0])

profitsDict = {"Name": f, "Intraday": totalIntradayProfitOfAllCompanies,
               "Investing": totalInvestingProfitOfAllCompanies}

df = pd.DataFrame(profitsDict)
df.to_csv(path_or_buf="DataSets/FinalProfits/INDIAFinalProfits.csv")