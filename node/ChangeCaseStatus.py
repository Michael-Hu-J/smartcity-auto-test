#!/usr/bin/python3
# -*- coding:utf-8 -*-

from common.HttpClientUtil import HttpClientUtil
from node.GetToken import GetToken
from node.ReportCase import ReportCase


class ChangeCaseStatus(HttpClientUtil):
    access_token = GetToken().get_token()
    casecode = ReportCase().report_case()

    def change_case_status(self):
        url = "https://172.26.55.39" + "/service/SmartCity3__CaseService/1.0.0/ChangeCaseStatus"
        data = {
            "handlingUser": {
                "orgCode": "ShangBaoZhongXin",
                "orgName": "苏州市上报中心",
                "postCode": "ShangBaoYuan",
                "postName": "上报员",
                "userCode": "jinkesi",
                "userName": "金克丝"
            },
            "action": "file",
            "caseCode": ChangeCaseStatus.casecode,
            "reason": "上报已完成",
            "comment": "立案",
            "extFieldValues": [
                {
                    "fieldName": "TASK_TYPE_FILE",
                    "childFieldValues": [
                        {
                            "fieldName": "tastype",
                            "fieldValue": "立案"
                        },
                        {
                            "fieldName": "result",
                            "fieldValue": "通过"
                        }
                    ]
                }
            ],
            "attachments": [
                {
                    "attachmentName": "立案bdlogo.png",
                    "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "access-token": ChangeCaseStatus.access_token
        }
        resp = super().post(url=url,headers=headers,json=data)
        print(resp.text)


if __name__ == '__main__':
    ChangeCaseStatus().change_case_status()