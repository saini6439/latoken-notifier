def get_token():
    import requests

    baseUrl = 'https://api.latoken.com'
    endpoint = '/v2/currency/available'
    url = baseUrl + endpoint

    response = requests.get(url)
    json_response = response.json()
    
    return json_response