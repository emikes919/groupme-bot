from flask import Flask

botApp = Flask(__name__)

@botApp.route('/')
def testFunc():
	try:
		print('hello sophie!')
	except:
		pass	
	return 'hello sophie!'

if __name__ == '__main__':
	botApp.run()