#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import urllib3
import json
import time

urllib3.disable_warnings()


class HttpClientUtil:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params, **kwargs):
        return self.session.request(url=url, method="get", params=params, verify=False, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.request(url=url, method="post", data=data, json=json, verify=False, **kwargs)
