#!/usr/bin/env python3
import requests
import base64
import urllib
try:
    temp_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=nGtAgM9eiLvcZTG7h0YkZTk5&client_secret=Xs5GWxd8CZON7fLKOgWlX5u8k2qco3h9'
    temp_res = requests.post(temp_url)
    temp_token = eval(temp_res.text)['access_token']
    temp_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + temp_token
    temp_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    temp_file = open('code_xjtu.jpg', 'rb')
    temp_image = temp_file.read()
    temp_file.close()
    temp_data = {
        'image': base64.b64encode(temp_image)
    }
    temp_data = urllib.parse.urlencode(temp_data)
    temp_res = requests.post(url=temp_url, data=temp_data, headers=temp_headers)
    code = int(eval(temp_res.text)['words_result'][0]['words'])
except Exception as e:
    print(e)
    print('error')
