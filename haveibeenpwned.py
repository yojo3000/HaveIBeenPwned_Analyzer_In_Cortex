#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import json
import requests
from cortexutils.analyzer import Analyzer

class haveibeenpwnedAnalyzer(Analyzer):

    def __init__(self):

        Analyzer.__init__(self)



    def do_something(self):

        URL             = "https://haveibeenpwned.com/api/v2/breachedaccount/"

        email_addr      = "hahaha@gmail.com"
        URL             += email_addr

        import cfscrape

        import pprint
        import time

        # token           = cfscrape.get_tokens('https://haveibeenpwned.com/api/v2/breachedaccount/test@example.com', user_agent='WTF')
        # cookies         = token[0]
        # user_agent      = token[1]


        # http_headers    = {
                # 'User-Agent': 'WTF'
                # }

        # sslVerify       = True


        try:

            time.sleep(1.5)

            response = requests.get(URL)
            # response = requests.get(URL, headers=http_headers, verify=sslVerify, cookies=cookies)

            status_code = response.status_code

            json_content = json.loads(response.content.decode('utf-8'))

        except Exception as e:
            print (e)

        return {'result': json_content}

    def summary(self, raw):
        temp_list = []
        temp_list.append("aaa")
        temp_list.append("bbb")

        temp = {"sum wtf": temp_list}

        return temp

    def run(self):

        self.report(
                self.do_something()
                )


if __name__ == '__main__':
    haveibeenpwnedAnalyzer().run()
