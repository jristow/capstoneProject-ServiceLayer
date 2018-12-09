import pandas as pd

a = pd.read_csv('Sale_Prices_Zip.csv')
b = pd.read_csv("zips.csv")
merged = a.merge(b, on='zip')
merged.to_csv("zipData.csv", index=False)