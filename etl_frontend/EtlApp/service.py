import os
import requests
import json
from django.conf import settings


service_url = settings.BACKEND_URL
#DATA = {'username':'brandiq-admins','password':'brandiq@123'}
def do_login(data):
  
    response_data = {}
    URL=service_url+"api/user/login/"
    print(URL)
    r = requests.post(url = URL, data = data)
    print("i am tester",r)
      
    # extracting data in json format
    #response_data['message'] = "error"
    response = r.json()
 
    print(response)
   

    return response
import requests

import random
import string

# Generate a random string of 10 characters
boundary = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# headers = {'Authorization': f'Bearer {toen}', 'Content-Type': f'multipart/form-data; boundary=----WebKitFormBoundary{boundary}'}
# data = f'------WebKitFormBoundary{boundary}\r\nContent-Disposition: form-data; name="file"; filename="example.txt"\r\nContent-Type: text/plain\r\n\r\nexample content\r\n------WebKitFormBoundary{boundary}--\r\n'

def file_upload(data,toen):
        URL=service_url+"api/user/file-upload/"
        print(URL)

        # headers = {'Authorization': f'Bearer {toen}', 'Content-Type': 'multipart/form-data'}
        headers = {'Authorization': f'Bearer {toen}', 'Content-Type': f'multipart/form-data; boundary=----WebKitFormBoundary{boundary}'}

        r = requests.post(url = URL, headers=headers, data = data["file"])
        print("i am tester",r)
        print(headers)
        
        # extracting data in json format
        #response_data['message'] = "error"
        response = r.json()
        print(response)
        return response
