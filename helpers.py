import requests

def get_answer():
    """Get an answer."""
    return True

def get_headers():
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    return headers

def get_html():
    url = "https://www.google.com"
    headers = get_headers()
    req = requests.get(url, headers)
    return req