import requests

url = "http://192.168.41.99:8000/api/actions/import"

payload = {}
files = [
    ('file', ('D:\00 Gitlab\cepri\topu\2-TO-2.ata', open('D:\\00 Gitlab\\cepri\\topu\\2-TO-2.ata', 'rb'),
              'application/octet-stream'))
]
headers = {
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Accept': '*/*',
    'Host': '192.168.41.99:8000',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=--------------------------442052209032232674222695'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, verify=False)

print(response.text)
