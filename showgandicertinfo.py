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

# Count your Gandi certs

GANDISITESNUMS = API.cert.count(APIKEY)

GANDISITE_COUNT_MSG = "You have %s certificate" % GANDISITESNUMS
if GANDISITESNUMS > 1:
    GANDISITE_COUNT_MSG += "s"
print GANDISITE_COUNT_MSG

#  Get all certs
CERT_LIST = []
for eachsite in API.cert.list(APIKEY):
    CERT_LIST.append(eachsite['id'])

print "Gandi CERT IDs:", CERT_LIST

#  Get info on each Gandi certs
if len(CERT_LIST) > 0:
    for certid in CERT_LIST:
        print API.cert.info(APIKEY, certid)
        print
