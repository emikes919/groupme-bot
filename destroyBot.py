import requests, config

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.destroyBotEndpoint
tokenParam = '?token=' + config.TOKEN

botIDs = [
	'f1a70d6bb90e3eb4e34514adbb',
	'e1d47bcb988cb16042e4c5b5f9',
	'c52bd83bd48276dcf8c6a2b2f0',
	'70f84f510622d4f86986c34687'
]

def destroyBot(bot):
	url = BASEURL + endpoint + tokenParam
	botParam = {'bot_id': bot}
	response = requests.post(url, json=botParam)
	print(response.status_code)
	return response

for id in botIDs:
	destroyBot(id)