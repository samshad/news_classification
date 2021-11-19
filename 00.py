import pandas as pd
import json


path = 'Data/News_Category_Dataset_v2.json'

list_ = []
with open(path) as files:
    for file in files:
        list_.append(json.loads(file))

data = pd.DataFrame(list_)
print(data.head().to_string())

data.to_csv('Data/News_Category_Dataset.csv', index=False)
