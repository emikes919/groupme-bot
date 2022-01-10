from flask import Flask, request
import pprint

botApp = Flask(__name__)

@botApp.get('/')
def placeholderText():
	return 'This is a placeholder page for Ed\'s Groupme chat boi API'

@botApp.post('/')
def recMessage():
	print('botAPI hit by Groupme, message received')
	if request.is_json:
		message = request.get_json()
		pprint.pprint(message)
		return 200
	return {'error': 'Request must be JSON'}, 415

if __name__ == '__main__':
	botApp.run()