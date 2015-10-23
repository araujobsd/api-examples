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

# Count your Gandi Sites

GandiSitesNums = api.site.count(apikey)

gandisite_count_msg = "You have %s Gandi Site" % GandiSitesNums
if GandiSitesNums > 1:
    gandisite_count_msg += "s"
print gandisite_count_msg

# Get all site id 
siteid_list = []
for eachsite in api.site.list(apikey):
    for k,v in eachsite.items():
        if k == "id":
            siteid_list.append(v)
print "Gandi Site IDs:", siteid_list

#Get info on each Gandi site
if len(siteid_list) > 0:
    for siteid in siteid_list:
        print api.site.info(apikey, siteid)
        print 


