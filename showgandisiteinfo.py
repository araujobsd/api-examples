# -*- coding: utf-8 -*-

"""
The sample code is to show info of your Gandi Site with API key.
此範例程式碼用途為透過API金鑰，取得Gandi Site相關資訊
"""

import xmlrpclib
import sys
from pprint import pprint

# Connect to the API server
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

# Count your Gandi Sites
# 計算Gandi Site的數量
GANDISITESNUMS = API.site.count(APIKEY)

GANDISITE_COUNT_MSG = "You have %s Gandi Site" % GANDISITESNUMS
if GANDISITESNUMS > 1:
    GANDISITE_COUNT_MSG += "s"
print GANDISITE_COUNT_MSG

#  Get all site id
#  取得所有Site編號
SITEID_LIST = []
for eachsite in API.site.list(APIKEY):
    SITEID_LIST.append(eachsite['id'])

print "Gandi Site IDs:", SITEID_LIST

#  Get info on each Gandi Site
#  取得各個Gandi Site的相關資訊
if len(SITEID_LIST) > 0:
    pprint(API.site.list(APIKEY))
