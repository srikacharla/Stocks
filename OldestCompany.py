from os import walk
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(f"DataSets/US"):
    f.extend(filenames)
    break
files = []
for name in f:
    files.append(pd.read_csv(f"DataSets/US/{name}"))
date = "2021-09-09"
finalName = ""
i = 0
finali = 0
for singleFile in files:
    column = singleFile.get(["Date"])
    print(column.get("Date")[0],f[i] )
    i += 1
    if column.get("Date")[0] < date:
        date = column.get("Date")[0]
        finalName = singleFile
        finali = i
print(f[finali])


