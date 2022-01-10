import requests, pprint, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.botsEndpoint
tokenParam = '?token=' + config.TOKEN

bot = config.bot

# create and register bot via POST request
def createBot():
	botParam = bot
	url = BASEURL + endpoint + tokenParam
	response = requests.post(url, json=botParam)
	print(response.status_code)
	return response

createBot()