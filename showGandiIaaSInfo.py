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
print "gandi api version:" + version['api_version']

# Count your Gandi IaaSs 

GandiIaaSNums = api.hosting.vm.count(apikey)

gandiiaas_count_msg = "You have %s Gandi IaaS Instance" % GandiIaaSNums
if GandiIaaSNums > 1:
    gandiiaas_count_msg += "s"
print gandiiaas_count_msg

# Get all IaaS id 
iaasid_list = []
for eachiaas in api.hosting.vm.list(apikey):
    iaasid_list.append(eachiaas['id'])

print "Gandi IaaS IDs:", iaasid_list

#Get info on each IaaSs
if len(iaasid_list) > 0:
    for iaasid in iaasid_list:
        print api.hosting.vm.info(apikey, iaasid)
        print 


