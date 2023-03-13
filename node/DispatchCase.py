#!/usr/bin/python3
# -*- coding:utf-8 -*-

from common.HttpClientUtil import HttpClientUtil
from node.GetToken import GetToken
from node.ReportCase import ReportCase


class DispatchCase(HttpClientUtil):
    access_token = GetToken().get_token()
    casecode = ReportCase().report_case()

    def dispatch_case(self):
        url = "https://172.26.55.39" + "/service/SmartCity3__CaseService/1.0.0/DispatchCase"
        data = {
            "handlingUser": {
                "orgCode": "FenBoZhongXin",
                "orgName": " 苏州市分拨中心",
                "postCode": "FenBoYuan",
                "postName": "分拨中心分拨员",
                "userCode": "szfbzxfby",
                "userName": "苏州分拨中心分拨员"
            },
            "caseCode": DispatchCase.casecode,
            "taskType": "TASK_TYPE_DISPATCH",
            "comment": "分拨",
            "attachments": [
                {
                    "attachmentName": "分拨bdlogo.png",
                    "attachmentUrl": "http://www.baidu.com/img/bdlogo.png"
                }
            ],
            "executorType": "Organization",
            "isCompulsive": "N",
            "cooperationType": "MainCo",
            "executors": [
                {
                    "isMaster": "Y",
                    "orderNo": 1,
                    "orgCode": "suzhoushichuzhibumen",
                    "orgName": "苏州市处置部门",
                    "postCode": "szsczbmczgw",
                    "postName": "苏州市处置部门处置岗位"
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "access-token": DispatchCase.access_token
        }
        resp = super().post(url=url,headers=headers,json=data)
        print(resp.text)


if __name__ == '__main__':
    DispatchCase().dispatch_case()