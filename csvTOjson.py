import csv
import json

csvFilePath = 'mplist1.csv'
jsonFilePath = 'mplist_new.json'

data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        key = rows['ID']
        data[key] = rows

with open(jsonFilePath, 'w') as jsonFile:

    jsonFile.write(json.dumps(data, indent=4))