import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


case_path = os.path.abspath(__file__)
dir_name, temp_filename = os.path.split(case_path)
file_name, extension = os.path.splitext(temp_filename)

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzA1NTgxMTE2LCJlbWFpbCI6InN1cHBvcnRAeGluZXJ0ZWwuY29tIn0.jeWklWZRmimWl5NjqS92N90R3GCJesVMB4rHDPJCrZE'
path = os.path.join(dir_name, 'file', 'demo.zip')
m = MultipartEncoder(fields={
    'project_name': (None, '项目一', None),
    'upload_file': ('demo.zip', open(path, 'rb'), 'application/x-zip-compressed')
})
headers = {
            'Content-Type': m.content_type,
            "Cookie": 'sessionid=htsn6i931eafuxh6zsoto44bbvsa3iq7',
            "Authorization": f'Bearer {token}'
        }

res = requests.post('http://10.0.9.28:8899/test_project/project/upload/', data=m, headers=headers)
print(res)
pass
