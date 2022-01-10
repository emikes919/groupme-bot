import requests, pprint, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.destroyBotEndpoint
tokenParam = '?token=' + config.TOKEN

botIDs = [
	''
]

def destroyBot(bot):
	url = BASEURL + endpoint + tokenParam
	botParam = {'bot_id': bot}
	response = requests.post(url, json=botParam)
	print(response.status_code)
	return response

for id in botIDs:
	destroyBot(id)