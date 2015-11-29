# -*- coding: utf-8 -*-

"""
The sample code is to show contact info with API key
此範例程式碼用途為透過API金鑰，取得聯絡人相關資訊
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

#  Get all handle ids
#  取得帳號ID
HANDLE_LIST = []
for eachcontact in API.contact.list(APIKEY):
    HANDLE_LIST.append(eachcontact['handle'])

print "Gandi Site IDs:", HANDLE_LIST

#  Get info on each Gandi handle
#  取得個別的Gandi帳號資料

if len(HANDLE_LIST) > 0:
    pprint(API.contact.list(APIKEY))
