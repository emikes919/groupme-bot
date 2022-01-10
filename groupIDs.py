import requests, pprint, config

# GroupMe API auth data
BASEURL = config.BASEURL
endpoint = config.groupsEndpoint
tokenParam = '?token=' + config.TOKEN

def getGroupID():
	url = BASEURL + endpoint + tokenParam
	response = requests.get(url)
	groupIDs = response.json()
	return(groupIDs)

pprint.pprint(getGroupID())