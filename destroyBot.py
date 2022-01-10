import requests, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.destroyBotEndpoint
tokenParam = '?token=' + config.TOKEN

botIDs = [
	'b6fc11735e9abf9730cd18d3aa',
	'9a3751e42793e52d8b17efa725'
]

def destroyBot(bot):
	url = BASEURL + endpoint + tokenParam
	botParam = {'bot_id': bot}
	response = requests.post(url, json=botParam)
	print(response.status_code)
	return response

for id in botIDs:
	destroyBot(id)