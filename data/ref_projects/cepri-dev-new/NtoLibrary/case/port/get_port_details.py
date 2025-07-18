import json
import os

from lib.nto.common import NTO

nto = NTO(host='192.168.41.99', port='8000', username='admin', password='admin')
res = nto.get(url='api/ports/PA05')
print(res)

case_path = os.path.abspath(__file__)
dir_name, temp_filename = os.path.split(case_path)
file_name, extension = os.path.splitext(temp_filename)

with open(os.path.join(dir_name, 'data', f'{file_name}.json'), 'w') as fid:
    json.dump(res, fid, indent=4, sort_keys=True)

pass
