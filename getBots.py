import requests, pprint, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.botsEndpoint
tokenParam = '?token=' + config.TOKEN

def getBots():
	url = BASEURL + endpoint + tokenParam
	botList = requests.get(url)
	pprint.pprint(botList.json())
	return botList

getBots()