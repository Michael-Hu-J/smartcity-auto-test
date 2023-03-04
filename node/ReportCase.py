#!/usr/bin/python3
# -*- coding:utf-8 -*-

from common.HttpClientUtil import HttpClientUtil
from node.FetchToken import FetchToken
import time


class ReportCase(HttpClientUtil):
    access_token = FetchToken().fetch_token()

    def report_case(self):
        url = "https://172.26.55.39" + "/service/SmartCity3__CaseService/1.0.0/ReportCase"
        data = {
            "attachments": [
                {
                    "attachmentName": "bdlogo.png",
                    "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
                }
            ],
            "caseName": "测试城运流程",
            "srcCaseId": "",
            "itemCode": "csshztwt",
            "categoryCode": "",
            "description": "十堰新城运加派",
            "occurrenceDate": "2022-07-17 10:00:00",
            "address": "苏州市",
            "latitude": "122.23",
            "longitude": "123.12",
            "cityCode": "",
            "districtCode": "",
            "streetCode": "",
            "communityCode": "",
            "gridCode": "heimaojingzhang",
            "channelId": "UrbanOperationApp",
            "channelType": "004",
            "reportPersonalInfo": {
                "contactName": "胡建",
                "mobilePhone": "17771432624",
                "needReVisit": "Y"
            },
            "severityLevel": "3",
            "urgencyLevel": "3",
            "handlingUser": {
                "orgCode": "ShangBaoZhongXin",
                "orgName": "苏州市上报中心",
                "postCode": "ShangBaoYuan",
                "postName": "上报员",
                "userCode": "jinkesi",
                "userName": "金克丝"
            },
            "tagCodes": [],
            "dutyOrgs": [
                {
                    "orgCode": "ShangBaoZhongXin"
                }
            ],
            "caseType": "2",
            "comment": "上报事件"
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "access-token": ReportCase.access_token
        }
        resp = super().post(url=url, headers=headers, json=data)
        cascode = resp.json()["result"]["caseCode"]
        time.sleep(3)
        return cascode
