# -*- coding: utf-8 -*-

"""
此範例程式碼用途為透過API金鑰，取得Gandi IaaS相關資訊
"""

import xmlrpclib
import sys
from pprint import pprint

#  Connect to the API server
#  連接API伺服器
API = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

if len(sys.argv) != 2:
    print "%s %s" % (sys.argv[0], "<YOUR API KEY>")
    exit(1)

APIKEY = sys.argv[1]

#  您可以呼叫API方法
#  您必須經由API金鑰作為第一個方法的參數進行驗證
VERSION = API.version.info(APIKEY)
print "gandi api version:" + VERSION['api_version']

#  Count your Gandi IaaSs
#  計算您的Gandi IaaS數量

GANDIIAASNUMS = API.hosting.vm.count(APIKEY)

GANDIIAAS_COUNT_MSG = "You have %s Gandi IaaS Instance" % GANDIIAASNUMS
if GANDIIAASNUMS > 1:
    GANDIIAAS_COUNT_MSG += "s"
print GANDIIAAS_COUNT_MSG

#  取得全部的IaaS編號
IAASID_LIST = []
for eachiaas in API.hosting.vm.list(APIKEY):
    IAASID_LIST.append(eachiaas['id'])

print "Gandi IaaS IDs:", IAASID_LIST

#  取得個別的IaaS資訊內容

if len(IAASID_LIST) > 0:
    pprint(API.hosting.vm.list(APIKEY))
