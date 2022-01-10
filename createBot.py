import requests, pprint, config

# Groupme Auth data
BASEURL = config.BASEURL
endpoint = config.botsEndpoint
tokenParam = '?token=' + config.TOKEN

bot = config.bot

# create and register bot via POST request
def createBot():
	headers = {'Content-type': 'application/json'}
	url = BASEURL + endpoint + tokenParam
	response = requests.post(url, json=bot, headers=headers)
	print(response.status_code)
	pprint.pprint(response)
	return response

createBot()