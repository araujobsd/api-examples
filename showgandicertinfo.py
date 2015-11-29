# -*- coding: utf-8 -*-
"""
The sample code is to show info of your Gandi SSL certificates with API key.
此範例程式碼用途為透過API金鑰，取得Gandi SSL憑證相關資訊
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

# Now you can call API methods.
# You must authenticate yourself by passing
# the API key as the first method's argument
#  您可以呼叫API方法
#  您必須經由API金鑰作為第一個方法的參數進行驗證
VERSION = API.version.info(APIKEY)
print "gandi api version: " + VERSION['api_version']

# Count your Gandi certs
# 計算Gandi憑證的數量
GANDISITESNUMS = API.cert.count(APIKEY)

GANDISITE_COUNT_MSG = "You have %s certificate" % GANDISITESNUMS
if GANDISITESNUMS > 1:
    GANDISITE_COUNT_MSG += "s"
print GANDISITE_COUNT_MSG

#  Get all certs
#  取得所有憑證
CERT_LIST = []
for eachsite in API.cert.list(APIKEY):
    CERT_LIST.append(eachsite['id'])

print "Gandi CERT IDs:", CERT_LIST

#  Get info on each Gandi certs
#  取得各個Gandi憑證的相關資訊

if len(CERT_LIST) > 0:
    pprint(API.cert.list(APIKEY))
