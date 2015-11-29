# -*- coding: utf-8 -*-

"""
The sample code is to show info of your Gandi zone file info with API key
此範例程式碼用途為透過API金鑰，取得Gandi區域檔的相關資訊
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

#  Now you can call API methods.
#  You must authenticate yourself by passing
#  the API key as the first method's argument
#  您可以呼叫API方法
#  您必須經由API金鑰作為第一個方法的參數進行驗證
VERSION = API.version.info(APIKEY)
print "gandi api version: " + VERSION['api_version']

#  list the zones you have access to
#  列出所有存取權限的區域檔
GANDIZONES = API.domain.zone.list(APIKEY)

GANDIZONE_MSG = "ZONE INFOMATION"
print GANDIZONE_MSG
pprint(GANDIZONES)
