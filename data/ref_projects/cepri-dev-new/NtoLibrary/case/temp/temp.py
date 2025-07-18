import base64
import json
import os.path

import requests

case_path = os.path.abspath(__file__)
dir_name, temp_filename = os.path.split(case_path)
file_name, extension = os.path.splitext(temp_filename)


class client:

    def __init__(self, host, port, token, content_type=None):
        self.base_url = f'https://{host}:{port}'
        if content_type is None:
            content_type = "application/json"
        self.headers = {
            # "Content-Type": content_type,
            "Cookie": 'sessionid=htsn6i931eafuxh6zsoto44bbvsa3iq7',
            "Authorization": f'Basic {token}'
        }

    def get(self, url, data=None):
        """
        获取信息

        Args:

            url (str): APLS设备URL地址

            data (dict): json参数字典

        Returns:

            dict: eg::

            {
                'id': 76,
                'name': 'test'
            }

        Examples:
            Python

        .. code:: Python

            nto = NTO(host='192.168.41.99.', port='8000', username='admin', password='admin')
            nto.get(url='/api/filters')

        """

        if data is None:
            res = requests.get(url=f'{self.base_url}/{url}', headers=self.headers, verify=False)
        else:
            res = requests.get(url=f'{self.base_url}/{url}', headers=self.headers, json=data, verify=False)
        return res.json()

    def post(self, url, data=None):
        """
        获取信息

        Args:

            url (str): APLS设备URL地址

            data (dict): json参数字典

        Returns:

            dict: eg::

            {
                'id': 76,
                'name': 'test'
            }

        Examples:
            Python

        .. code:: Python

            nto = NTO(host='192.168.41.99.', port='8000', username='admin', password='admin')
            nto.get(url='/api/filters')

        """

        if data is None:
            res = requests.post(url=f'{self.base_url}/{url}', headers=self.headers, verify=False)
        else:
            res = requests.post(url=f'{self.base_url}/{url}', headers=self.headers, data=data, verify=False)
        return res.json()


if __name__ == '__main__':
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzA1NTgxMTE2LCJlbWFpbCI6InN1cHBvcnRAeGluZXJ0ZWwuY29tIn0.jeWklWZRmimWl5NjqS92N90R3GCJesVMB4rHDPJCrZE'
    client = client('10.0.9.28', '8899', token, 'multipart/form-data')
    path = os.path.join(dir_name, 'file', 'demo.zip')
    fileObject = {
        'project_name': (None, '项目一', None),
        'upload_file': ('demo.zip', open(path, 'rb'), 'application/x-zip-compressed', {'Expires': '0'})
    }
    res = requests.post(url=f'{client.base_url}/test_project/project/upload/', headers=client.headers, files=fileObject, verify=False)
    print(res)
    pass
