import requests


def handler(event, context):
    return requests.get('https://api.ipify.org').text
