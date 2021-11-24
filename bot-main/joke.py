import os
import requests
import json

def get_joke():
    headers = {'user-agent': 'contact@colinpeterson.ca', 'Accept': 'application/json'}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    return(r.json()['joke'])
    


