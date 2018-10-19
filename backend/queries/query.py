import urllib3
import requests
from requests.auth import HTTPBasicAuth
import logging

class MakeQuery:
    def __init__(self):
        urllib3.disable_warnings()
        self.user = "RO"
        self.cmxPwd = "just4reading"
        self.statPwd = "Passw0rd"
        logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename='error.log',
            level=logging.WARNING)
    def cmx(self, url):
        try:
            res = requests.get(url=url, auth=HTTPBasicAuth(self.user, self.cmxPwd), verify=False)
            if res:
                return res
            logging.info("Request %s %s", url , " get back empty result")
        except requests.exceptions.RequestException as e:
            logging.warning("Request %s %s %s", url, "make exception ", e)

    def statistic(self, url):
        try:
            res = requests.get(url=url, auth=HTTPBasicAuth(self.user, self.statPwd), verify=False)
            if res:
                return res
            logging.info("Request %s %s", url, " get back empty result")
        except requests.exceptions.RequestException as e:
            logging.warning("Request %s %s %s", url, "make exception ", e)


class GetQuery:
    aesUid = ""
    def __init__(self):
        self.query = MakeQuery()
        if GetQuery.aesUid == "":
            GetQuery.aesUid = self.query.statistic('https://cisco-presence.unit.ua/api/config/v1/sites').json()[0]['aesUidString']

requestServer = GetQuery()