import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    
    data_raw = requests.get(url).text
    data = json.loads(data_raw)
    
    # top_artist = data['topartist']
    # print(top_artist)
    return data['topartists']['artist'][0]['name'] # return the top artist in Spain


# NECESITAMOS TOKEN DE LAST.FM