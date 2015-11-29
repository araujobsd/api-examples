# -*- coding: utf-8 -*-

"""
The sample code is to show info of your Gandi PaaS instances with API key.
此範例程式碼用途為透過API金鑰，取得Gandi IaaS相關資訊
"""

import xmlrpclib
import sys

#  Connect to the API server
#  連接API伺服器
API = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

if len(sys.argv) != 2:
    print "%s %s" % (sys.argv[0], "<YOUR API KEY>")
    exit(1)

APIKEY = sys.argv[1]

#  Now you can call API methods.
#  You must authenticate yourself by passing
#  the API key as the first method's argument
#  您可以呼叫API方法
#  您必須經由API金鑰作為第一個方法的參數進行驗證
VERSION = API.version.info(APIKEY)
print "gandi api version: " + VERSION['api_version']

#  Count your Gandi PaaS instances
#  計算Gandi Paas 實體的數量
GANDIPAASNUMS = API.paas.count(APIKEY)

GANDIPAAS_COUNT_MSG = "You have %s Gandi PaaS Instance" % GANDIPAASNUMS
if GANDIPAASNUMS > 1:
    GANDIPAAS_COUNT_MSG += "s"
print GANDIPAAS_COUNT_MSG

#  Get all site id
#  取得所有site 編號
PAASID_LIST = []
for eachpaas in API.paas.list(APIKEY):
    PAASID_LIST.append(eachpaas['id'])

print "Gandi PaaS IDs:", PAASID_LIST

#  Get info on each Gandi Site
#  取得所有Gandi Site 的相關資訊
if len(PAASID_LIST) > 0:
    pprint(API.paas.list(APIKEY))
