import requests
import urllib3
import json
import time

urllib3.disable_warnings()


class HttpUtil:
    access_token = None
    caseCode = None

    def __init__(self):
        self.session = requests.Session()

    def fetch_token(self):
        payload = {
            "grant_type": "client_credentials",
            "client_id": "7cbc31a7a11548f79a891fcd8e6ea9b2",
            "client_secret": "983d94f8e9f6ff45704e9892ad4abdedfd82d39759ec3dbd"
        }
        resp = self.session.request(method="post", url="https://172.26.55.39/baas/auth/v1.0/oauth2/token", data=payload,
                                        verify=False)
        HttpUtil.access_token = resp.json()["access_token"]
        print(HttpUtil.access_token)

    def city_report(self):
        payload = {
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
            "access-token": HttpUtil.access_token
        }
        resp = self.session.request(method="post",
                                    url="https://172.26.55.39/service/SmartCity3__CaseService/1.0.0/ReportCase",
                                    headers=headers, json=payload, verify=False)
        HttpUtil.caseCode = resp.json()["result"]["caseCode"]
        print(resp.json())

    def city_file(self):
        payload = {
            "handlingUser": {
                "orgCode": "ShangBaoZhongXin",
                "orgName": "苏州市上报中心",
                "postCode": "ShangBaoYuan",
                "postName": "上报员",
                "userCode": "jinkesi",
                "userName": "金克丝"
            },
            "action": "file",
            "caseCode": HttpUtil.caseCode,
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
            "access-token": HttpUtil.access_token
        }
        resp = self.session.request(method="post",
                                    url="https://172.26.55.39/service/SmartCity3__CaseService/1.0.0/ChangeCaseStatus",
                                    headers=headers, json=payload, verify=False)
        print(resp.json())

    def city_dispatch(self):
        payload = {
            "handlingUser": {
                "orgCode": "FenBoZhongXin",
                "orgName": " 苏州市分拨中心",
                "postCode": "FenBoYuan",
                "postName": "分拨中心分拨员",
                "userCode": "szfbzxfby",
                "userName": "苏州分拨中心分拨员"
            },
            "caseCode": HttpUtil.caseCode,
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
            "access-token": HttpUtil.access_token
        }
        resp = self.session.request(method="post",
                                    url="https://172.26.55.39/service/SmartCity3__CaseService/1.0.0/DispatchCase",
                                    headers=headers, json=payload, verify=False)
        print(resp.json())


if __name__ == '__main__':
    HttpUtil().fetch_token()
    # HttpUtil().city_report()
    # time.sleep(3)
    # HttpUtil().city_file()
    # time.sleep(3)
    # HttpUtil().city_dispatch()
