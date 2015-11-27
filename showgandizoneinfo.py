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

GANDIZONES = API.domain.zone.list(APIKEY)

GANDIZONE_MSG = "ZONE INFOMATION"
print GANDIZONE_MSG 
print GANDIZONES

