import pandas as pd
import requests

def get_odata(target_url):
    data = pd.DataFrame()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
    while target_url:
        r = requests.get(target_url,headers=headers).json()
        r.raise_for_status()
        data = data.append(pd.DataFrame(r['value']))
        
        if '@odata.nextLink' in r:
            target_url = r['@odata.nextLink']
        else:
            target_url = None
            
    return data

