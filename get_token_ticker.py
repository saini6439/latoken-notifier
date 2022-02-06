def get_token():
    import requests

    baseUrl = 'https://api.latoken.com'
    endpoint = '/v2/ticker'
    url = baseUrl + endpoint

    response = requests.get(url)
    json_response = response.json()
    #print("json_response",json_response)
    return json_response