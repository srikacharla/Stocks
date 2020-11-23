from os import walk
import pandas as pd
import numpy as np

f = []
for (dirpath, dirnames, filenames) in walk(f"DataSets/US"):
    f.extend(filenames)
    break
print(f)
files = []
for name in f:
    files.append(pd.read_csv(f"DataSets/US/{name}"))
profitsDict = {}
totalIntradayProfitOfAllCompanies = list()
totalInvestingProfitOfAllCompanies = list()
for i in range(0, len(files)):
    columns = files[i].get(["Date", "Open", "Close"])
    datesAsNumpy = columns.Date.array.to_numpy()
    index = np.where(datesAsNumpy == "2017-08-02")
    closeAsNumpy = columns.Close.array.to_numpy()
    openAsNumpy = columns.Open.array.to_numpy()
    startingCloseValue = closeAsNumpy[index]
    endingCloseValue = closeAsNumpy[-1]
    startingToClosingCloseValues = closeAsNumpy[index[0].tolist()[0]:-1]
    startingToClosingOpenValues = openAsNumpy[index[0].tolist()[0]:-1]

    totalIntradayProfit = 0
    for index1 in range(0, len(startingToClosingCloseValues)):
        totalIntradayProfit += (startingToClosingCloseValues[index1] - startingToClosingOpenValues[index1])
    totalIntradayProfitOfAllCompanies.append(totalIntradayProfit)
    totalInvestingProfitOfAllCompanies.append(endingCloseValue - startingCloseValue[0])
profitsDict = {"Name": f, "Intraday": totalIntradayProfitOfAllCompanies,
               "Investing": totalInvestingProfitOfAllCompanies}

df = pd.DataFrame(profitsDict)
df.to_csv(path_or_buf="DataSets/FinalProfits/FinalProfits.csv")