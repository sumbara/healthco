import pandas as pd
import numpy as np

df_data = pd.read_csv('./static/hospital_location.csv', encoding='CP949')

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "KakaoAK YourAppKey"}
    result = json.loads(str(requests.get(url,headers=headers).text))
    match_first = result['documents'][0]['address']

    return float(match_first['y']),float(match_first['x'])