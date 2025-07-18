import requests

url = "https://192.168.41.99:8000/api/actions/import"

payload = {}
files = [
    ('file', (r'D:\00 Gitlab\cepri\topu\2-TO-2.ata', open(r'D:\00 Gitlab\cepri\topu\2-TO-2.ata', 'rb'),
              'application/octet-stream')),
    ('import_req_spec', ('import_type', 'FULL_IMPORT_FROM_BACKUP', 'application/json'))
]
headers = {
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, verify=False)

print(response.text)
