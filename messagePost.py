import requests, pprint, config, random

# Groupme Auth data
GROUPID = config.GROUPID
BASEURL = config.BASEURL
endpoint = config.postEndpoint
tokenParam = '?token=' + config.TOKEN
botID = config.botID
messageList = config.messageList

num = random.randint(0, len(messageList) - 1)
text = messageList[num]

def messagePost(message):
	url = BASEURL + endpoint + tokenParam
	message = {
		'bot_id': botID,
		'text': message
	}
	response = requests.post(url, json=message)
	print(response.status_code)
	return response

messagePost(text)