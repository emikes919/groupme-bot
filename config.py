# README
"""
Step 1: run groupIDs.py and select the group ID 
of the group you want to create the bot in

Step 2: set GROUPID below to the relevant group ID

Step 3: set the targetUserID to the person you want
the bot to respond to 

Step 4: name the bot in the bot dict below

Step 5: run createBot.py

Step 6: run getBots.py, find the bot you just created,
and enter the bot ID into the botID below

Step 7: commit to git and push to heroku

"""

# auth
TOKEN = ''
GROUPID = ''
BASEURL = 'https://api.groupme.com/v3'

# endpoints
groupsEndpoint = '/groups'
botsEndpoint = '/bots'
destroyBotEndpoint = '/bots/destroy'
postEndpoint = '/bots/post'

# API
callbackURL = ''
targetUserID = ''

# bot & message
bot = {
		'bot': {
			'name': 'Will\'s Conscience',
			'group_id': GROUPID,
			'callback_url': callbackURL
		}
	}
	
botID = ''
messageList = [
	''
]
