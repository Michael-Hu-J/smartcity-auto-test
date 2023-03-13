#!/usr/bin/python3
# -*- coding:utf-8 -*-

from common.HttpClientUtil import HttpClientUtil


class GetToken(HttpClientUtil):
    def get_token(self):
        url = "https://172.26.55.39" + "/baas/auth/v1.0/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": "7cbc31a7a11548f79a891fcd8e6ea9b2",
            "client_secret": "983d94f8e9f6ff45704e9892ad4abdedfd82d39759ec3dbd"
        }
        resp = super().post(url=url, data=data)
        access_token = resp.json()["access_token"]
        return access_token



