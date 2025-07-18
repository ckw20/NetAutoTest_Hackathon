import os
import requests, json, random, string
from requests_toolbelt import MultipartEncoder


def send_resp():
    import_req_spec = {
        "import_type": 'FULL_IMPORT_FROM_BACKUP',
    }

    url = "https://192.168.41.99:8000/api/actions/import"
    body = MultipartEncoder(fields={"import_req_spec": json.dumps(import_req_spec), "file": r'D:\00 Gitlab\cepri\topu\2-TO-2.ata'},
                            boundary=''.join(random.sample(string.ascii_letters + string.digits, 30))
                            )

    headers = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        "Content-Type": body.content_type
    }

    resp = requests.post(url, data=body, headers=headers, verify=False)
    print(resp.json())

send_resp()
