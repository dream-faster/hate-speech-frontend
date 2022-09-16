from enum import Enum
import requests

class Endpoints(Enum):
    local = "http://127.0.0.1:5000"
    remote = "https://intense-mountain-25095.herokuapp.com/detect"


def fetch(URL:str, PARAMS:dict)->dict:
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    
    return data
    

def get_prediction(text_to_predict: str, pipeline_name:str = 'random'):
    URL = f"{Endpoints.local.value}/detect"
    PARAMS = {'text':text_to_predict, "pipeline_name": pipeline_name}

    data = fetch(URL, PARAMS)
    
    return data['result']

def get_hierarchy(pipeline_name:str = 'random'):
    URL = f"{Endpoints.local.value}/pipeline"
    PARAMS = {"pipeline_name": pipeline_name}

    data = fetch(URL, PARAMS)
    print(data)
    return data['hierarchy']