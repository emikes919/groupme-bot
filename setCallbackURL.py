import requests, config, pprint

# Groupme Auth data
BASEURL = config.BASEURL
endpoint = config.botsEndpoint
tokenParam = '?token=' + config.TOKEN

callbackURL = config.callbackURL
bot = config.bot
bot['bot']['callback_url'] = callbackURL

def setCallbackURL():
	headers = {'Content-type': 'application/json'}
	url = BASEURL + endpoint + tokenParam
	response = requests.post(url, json=bot, headers=headers)
	return response

setCallbackURL()