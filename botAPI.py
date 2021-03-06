from flask import Flask, request
import pprint, requests, config, messagePost

botApp = Flask(__name__)

@botApp.get('/')
def placeholderText():
	return 'This is a placeholder page for Ed\'s Groupme chatbot API'

@botApp.post('/')
def recMessage():
	print('botAPI hit by Groupme, message received')
	if request.is_json:
		incomingMessage = request.get_json()
		pprint.pprint(incomingMessage)
		
		# bot conditional post message code
		if incomingMessage['sender_id'] == config.targetUserID:
			if len(incomingMessage['text']) >= 50000:
				messagePost.sendMessage()

		return 'Success!', 200
	return {'error': 'Request must be JSON'}, 415

if __name__ == '__main__':
	botApp.run()