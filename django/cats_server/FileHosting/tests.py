import json
import requests

# Create your tests here.

def request_file_test():
    url = "http://127.0.0.1:8000/FileHosting/file/"
    files = {'file': open('backup.json', 'rb'),
             'file_name': 'test'},
    response = requests.post(url = url, files = files)
    print(response)

request_file_test()