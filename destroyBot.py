import requests, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.destroyBotEndpoint
tokenParam = '?token=' + config.TOKEN

botIDs = [
	'dce896d8c57ac9b6e7e86107db'
]

def destroyBot(bot):
	url = BASEURL + endpoint + tokenParam
	botParam = {'bot_id': bot}
	response = requests.post(url, json=botParam)
	print(response.status_code)
	return response

for id in botIDs:
	destroyBot(id)