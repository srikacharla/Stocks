import pandas as pd
import numpy as np
from os import walk
from shutil import copyfile


file = (pd.read_csv(f"DataSets/FinalProfits/INDIAFinalProfits.csv"))

columns = file.get(["Name", "Intraday", "Investing"])

# print(columns)

IntradayProfits = np.array(columns.get("Intraday"))
print("Intraday: ",np.sum(IntradayProfits))

InvestingProfits = np.array(columns.get("Investing"))
print("Investing: ",np.sum(InvestingProfits))

