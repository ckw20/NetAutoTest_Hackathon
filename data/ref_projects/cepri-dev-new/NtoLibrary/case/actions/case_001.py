import http.client
import mimetypes
from codecs import encode

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

conn = http.client.HTTPSConnection("192.168.41.99", 8000)
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=import_req_spec;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("{\"import_type\":\"FULL_IMPORT_FROM_BACKUP\"}"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('D:\\00 Gitlab\\cepri\\topu\\2-TO-2.ata')))

fileType = mimetypes.guess_type('D:\\00 Gitlab\\cepri\\topu\\2-TO-2.ata')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open(r'D:\00 Gitlab\cepri\topu\2-TO-2.ata', 'rb') as f:
   dataList.append(f.read())
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
   'Authorization': 'Basic YWRtaW46YWRtaW4=',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': '192.168.41.99:8000',
   'Connection': 'keep-alive',
   'Content-Type': 'multipart/form-data; boundary=--------------------------442052209032232674222695',
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/api/actions/import", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
