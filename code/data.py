import json
import pandas as pd

def getDataframe():
    data = json.load(open('./data/device-covid19serology-0001-of-0001.json'))
    return pd.DataFrame(data["results"])
