import xmlrpclib
import sys

# Connect to the API server
api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

if len(sys.argv) != 2:
    print "%s %s" % (sys.argv[0], "<YOUR API KEY>")
    exit(1)

apikey = sys.argv[1]

# Now you can call API methods.
# You must authenticate yourself by passing
# the API key as the first method's argument
version = api.version.info(apikey)
print "gandi api version: " + version['api_version']

# Count your Gandi PaaS instances

GandiPaaSNums = api.paas.count(apikey)

gandipaas_count_msg = "You have %s Gandi PaaS Instance" % GandiPaaSNums
if GandiPaaSNums > 1:
    gandipaas_count_msg += "s"
print gandipaas_count_msg

# Get all site id 
paasid_list = []
for eachpaas in api.paas.list(apikey):
    paasid_list.append(eachpaas['id'])

print "Gandi PaaS IDs:", paasid_list

#Get info on each Gandi site
if len(paasid_list) > 0:
    for paasid in paasid_list:
        print api.paas.info(apikey, paasid)
        print 


