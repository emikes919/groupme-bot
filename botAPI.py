from flask import Flask

botApp = Flask(__name__)

@botApp.route('/')
def testFunc():
	print('hello sophie!')

if __name__ == '__main__':
	botApp.run()