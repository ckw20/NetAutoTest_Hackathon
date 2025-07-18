import base64
import json
import os.path
import time
import requests

from ruamel.yaml import YAML
from config.param import Config
from CustomLibrary.common import printf


class NTO:

    def __init__(self, host, port, username, password, content_type=None):
        self.base_url = f'https://{host}:{port}'
        self.host = host
        self.port = port
        encoded_str = base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode()
        if content_type is None:
            content_type = "application/json"
        self.headers = {
            "Content-Type": content_type,
            "Authorization": f'Basic {encoded_str}'
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

    def actions_import(self, path):
        # with open(os.path.abspath(path), 'rb+') as fid:
        #     data = fid.read()
        #     res = self.post(url='api/actions/import', data=
        #         {
        #             'import_req_spec': {
        #                 "import_type": 'FULL_IMPORT_FROM_BACKUP',
        #             },
        #         }
        #     )
        #     printf('NTO import tupo finish')
        #     return res
        yaml = YAML(typ='safe')
        Config.parse()
        Config.save()
        Config.check()
        with open(os.path.abspath(Config.param.variable), 'r', encoding='utf-8') as fid:
            variable = yaml.load(fid)
            if not variable['AUTO_TOPU']:
                return True
            else:

                import http.client
                import mimetypes
                from codecs import encode

                import ssl

                ssl._create_default_https_context = ssl._create_unverified_context

                conn = http.client.HTTPSConnection(self.host, self.port)
                dataList = []
                boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
                dataList.append(encode('--' + boundary))
                dataList.append(encode('Content-Disposition: form-data; name=import_req_spec;'))

                dataList.append(encode('Content-Type: {}'.format('application/json')))
                dataList.append(encode(''))

                dataList.append(encode("{\"import_type\":\"FULL_IMPORT_FROM_BACKUP\"}"))
                dataList.append(encode('--' + boundary))
                dataList.append(encode(
                    'Content-Disposition: form-data; name=file; filename={0}'.format(os.path.abspath(path))))

                fileType = mimetypes.guess_type(os.path.abspath(path))[0] or 'application/octet-stream'
                dataList.append(encode('Content-Type: {}'.format(fileType)))
                dataList.append(encode(''))

                with open(os.path.abspath(path), 'rb') as f:
                    dataList.append(f.read())
                dataList.append(encode('--' + boundary + '--'))
                dataList.append(encode(''))
                body = b'\r\n'.join(dataList)
                payload = body
                headers = {
                    'Authorization': 'Basic YWRtaW46YWRtaW4=',
                    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                    'Accept': '*/*',
                    'Host': f'{self.host}:{self.port}',
                    'Connection': 'keep-alive',
                    'Content-Type': 'multipart/form-data; boundary=--------------------------442052209032232674222695',
                    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
                }
                conn.request("POST", "/api/actions/import", payload, headers)
                res = conn.getresponse()
                data = res.read()
                print(data.decode("utf-8"))
                time.sleep(15)
                printf('NTO import tupo finish')
                return data.decode("utf-8")
