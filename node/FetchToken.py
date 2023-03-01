#!/usr/bin/python3
# -*- coding:utf-8 -*-

from common.HttpClientUtil import HttpClientUtil


def fetch_token():
    url = "/baas/auth/v1.0/oauth2/token"
    HttpClientUtil.post()