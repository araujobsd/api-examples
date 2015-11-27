"""
The sample code is to show info of your Gandi PaaS instances with API key.
"""

import xmlrpclib
import sys

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
print "gandi api version: " + VERSION['api_version']

#  Count your Gandi PaaS instances

GANDIPAASNUMS = API.paas.count(APIKEY)

GANDIPAAS_COUNT_MSG = "You have %s Gandi PaaS Instance" % GANDIPAASNUMS
if GANDIPAASNUMS > 1:
    GANDIPAAS_COUNT_MSG += "s"
print GANDIPAAS_COUNT_MSG

#  Get all site id
PAASID_LIST = []
for eachpaas in API.paas.list(APIKEY):
    PAASID_LIST.append(eachpaas['id'])

print "Gandi PaaS IDs:", PAASID_LIST

#  Get info on each Gandi site

if len(PAASID_LIST) > 0:
    pprint (API.paas.list(APIKEY))

