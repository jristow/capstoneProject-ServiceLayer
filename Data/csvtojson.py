import csv
import json 

with open("zipData.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('zipData.json', 'w') as f:
    json.dump(rows, f)