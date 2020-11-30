from os import walk
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(f"DataSets/US"):
    f.extend(filenames)
    break
files = []
oldestCompanyFile = []

for name in f:
    files.append(pd.read_csv(f"DataSets/US/{name}"))
    if name == "CAT.csv":
        oldestCompanyFile = files[-1]

columns = []
i = 0
for i in range(0, len(files)):
    columns = files[i].get(["Date", "Open", "Close"])
    oldestDates = oldestCompanyFile.get(["Date"])
    differenceInLength = len(oldestDates) - len(
        columns.get(["Date"]))
    newerCompanyColumnOpen = ([0] * differenceInLength) + list(
        columns.get("Open"))
    newerCompanyColumnClose = ([0] * differenceInLength) + list(
        columns.get("Close"))

    dict = {'Date': oldestCompanyFile.get("Date"), "Open": newerCompanyColumnOpen, "Close": newerCompanyColumnClose}
    df = pd.DataFrame(dict)

    fileName = f[i]
    df.to_csv(path_or_buf="DataSets/Blah/" + fileName)
    i += 1

oldestDates = oldestCompanyFile.get(["Date"])

print(len(files))
