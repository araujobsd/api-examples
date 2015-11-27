"""
The sample code is to show info of your Gandi IaaSs with API key.
"""

import xmlrpclib
import sys
from pprint import pprint

#  Connect to the API server
API = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

if len(sys.argv) != 2:
    print "%s %s" % (sys.argv[0], "<YOUR API KEY>")
    exit(1)

APIKEY = sys.argv[1]

#  Now you can call API methods.
#  You must authenticate yourself by passing
#  the API key as the first method's argument
VERSION = API.version.info(APIKEY)
print "gandi api version:" + VERSION['api_version']

#  Count your Gandi IaaSs

GANDIIAASNUMS = API.hosting.vm.count(APIKEY)

GANDIIAAS_COUNT_MSG = "You have %s Gandi IaaS Instance" % GANDIIAASNUMS
if GANDIIAASNUMS > 1:
    GANDIIAAS_COUNT_MSG += "s"
print GANDIIAAS_COUNT_MSG

#  Get all IaaS id
IAASID_LIST = []
for eachiaas in API.hosting.vm.list(APIKEY):
    IAASID_LIST.append(eachiaas['id'])

print "Gandi IaaS IDs:", IAASID_LIST

#  Get info on each IaaSs
if len(IAASID_LIST) > 0:
    pprint (API.hosting.vm.list(APIKEY))


