"""
The sample code is to show info of your Gandi Site with API key.
"""

import xmlrpclib
import sys

# Connect to the API server
API = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

if len(sys.argv) != 2:
    print "%s %s" % (sys.argv[0], "<YOUR API KEY>")
    exit(1)

APIKEY = sys.argv[1]

# Now you can call API methods.
# You must authenticate yourself by passing
# the API key as the first method's argument
VERSION = API.version.info(APIKEY)
print "gandi api version: " + VERSION['api_version']

#  Get all handle ids
HANDLE_LIST = []
for eachcontact in API.contact.list(APIKEY):
    HANDLE_LIST.append(eachcontact['handle'])

print "Gandi Site IDs:", HANDLE_LIST

#  Get info on each Gandi handle
if len(HANDLE_LIST) > 0:
    for contactid in HANDLE_LIST:
        print API.contact.info(APIKEY, contactid)
        print
