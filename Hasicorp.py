import json
from requests import Session
from requests_pkcs12 import Pkcs12Adapter

def hashicorp_vault(pfx_path, pfx_password, vaultdomain, valutloginurl, secretspath):
    '''
    Authenticate and Login to hashicorp vault and get the secrets
    Arguments:
        pfx_path      - pfx certificate full location
        pfx_password  - password of pfx certificate
        vaultdomain      - vault domain name
        valutloginurl - login url 
        secretspath   - path of the secrets one wants to fetch
    Returns:
        Secrets from the specified path in JSON Format
    '''
    with Session() as s:
        s.mount(vaultdomain, Pkcs12Adapter(pkcs12_filename= pfx_path,pkcs12_password=pfx_password))
        payload = json.dumps({
                "name": ""
        })
        headers = {
            'X-Vault-Request': 'true',
            'X-Vault-Namespace': '',
            'Content-Type': 'application/json'
        }
        r = s.put(valutloginurl, data=payload, headers=headers)
    jsondata = json.loads(r.content)
    if jsondata['auth']:
        token = jsondata['auth']['client_token']
        with Session() as s:
            payload = '' 
            headers = {
                'X-Vault-Request': 'true',
                'X-Vault-Namespace': '',
                'X-Vault-Token': token
                }
            secrets = s.get(secretspath, data=payload, headers=headers)
            resjsondata = json.loads(secrets.content)
    return resjsondata
