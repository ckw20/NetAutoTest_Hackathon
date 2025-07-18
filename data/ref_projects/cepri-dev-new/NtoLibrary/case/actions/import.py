from lib.nto.common import NTO

nto = NTO(host='192.168.41.99', port='8000', username='admin', password='admin', content_type='multipart/form-data')

with open(r'D:\00 Gitlab\cepri\topu\2-TO-2.ata', 'rb+') as fid:
    data = fid.read()
    res = nto.post(url='api/actions/import', data=
    {
        'import_req_spec': {
            "import_type": 'FULL_IMPORT_FROM_BACKUP',
        },
        'file': data
    }
                   )
    print(res)
pass
