import requests, pprint, config, random

# Groupme Auth data
BASEURL = config.BASEURL
endpoint = config.postEndpoint
tokenParam = '?token=' + config.TOKEN
botID = config.botID
messageList = config.messageList

def sendMessage():
	num = random.randint(0, len(messageList) - 1)
	text = messageList[num]
	url = BASEURL + endpoint + tokenParam
	message = {
		'bot_id': botID,
		'text': text
	}
	response = requests.post(url, json=message)
	print(response.status_code)
	return response