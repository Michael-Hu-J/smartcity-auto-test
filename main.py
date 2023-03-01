import requests
import urllib3
urllib3.disable_warnings()

req = requests.Session()
headers = {""}
body = {"grant_type": "client_credentials", "client_id": "7cbc31a7a11548f79a891fcd8e6ea9b2",
        "client_secret": "983d94f8e9f6ff45704e9892ad4abdedfd82d39759ec3dbd"}
resp = req.post(url="https://172.26.55.39/baas/auth/v1.0/oauth2/token", data=body,verify=False)
print(resp.text)
