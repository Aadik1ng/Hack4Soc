import http.client, urllib.parse
import json
conn = http.client.HTTPSConnection('api.marketaux.com')
api_token='fTW5EVeBM0ijnYIVT63uaFm9FVuDeXRMwb5R6Hv2'


def switch(risk,limit):
    if risk == "High":
        params = urllib.parse.urlencode({
    'api_token': api_token,
    'countries': 'in',
    'limit': limit,
    'sentiment_lte':0.5,
    # 'industries':'Technology'
    })
        conn.request('GET', '/v1/news/all?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        return data
    
    
    elif risk == "Medium":
        params = urllib.parse.urlencode({
    'api_token': api_token,
    'countries': 'in',
    'limit': limit,
    'sentiment_lte':0.095
    })
        conn.request('GET', '/v1/news/all?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        return data

    elif risk == "Low":
        params = urllib.parse.urlencode({
    'api_token': api_token,
    'countries': 'in',
    'limit': limit,
    'sentiment_lte':0.001
    
    })
        conn.request('GET', '/v1/news/all?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        return data






risk=str(input("Risk level "))
limit=4
data=switch(risk,3)

data=data.decode('utf-8')
json_data = json.loads(data)
formatted_json = json.dumps(json_data, indent=4)

print(formatted_json)
    