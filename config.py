# README
"""
Step 1: run groupIDs.py and select the group ID 
of the group you want to create the bot in

Step 2: set GROUPID below to the relevant group ID

Step 3: name the bot in the bot dict below

Step 4: run createBot.py

Step 5: run getBots.py, find the bot you just created,
and enter the bot ID into the botID below

Step 6: commit to git and push to heroku

"""

# auth
TOKEN = 'GHP3STkQhLJITckZ281ESBS4NfRYdpfKZ4SpAf39'
GROUPID = '84147785'
BASEURL = 'https://api.groupme.com/v3'

# endpoints
groupsEndpoint = '/groups'
botsEndpoint = '/bots'
destroyBotEndpoint = '/bots/destroy'
postEndpoint = '/bots/post'

# API
callbackURL = 'https://groupme-bot-ed1.herokuapp.com'
targetUserID = '3269722'

# bot & message
bot = {
		'bot': {
			'name': 'Will\'s Conscience',
			'group_id': GROUPID,
			'callback_url': callbackURL
		}
	}
	
botID = '000c08345da304e38b80f393a3'
messageList = [
	'dammit Will! remember what we talked about! Think before I type. Think before I type. Think before I type.',
	'what I really meant to say was: Hi I\'m Will, I\'m a big dumb idiot',
	'FUCK. i shouldn\'t have said that, i\'m so insecure! At least I\'m not as short as Ed, Steve or, heaven forbid, Sam',
	'blah blah blah, i\'m a silly moron',
	'I wish I could say what I\'m actually thinking. i love big dongs in my face',
	'i just want to take a second to let everyone know, I have a huge penis. Just kidding! It\'s tiny!',
	'I wonder if anyone knows I want to blow mike',
	'why can\'t I get "joel is hot" out of my dang head!',
	'I hope the fellas don\'t realize I\'m an easy target',
	'I love you Wes. Wait did I say that out loud?',
	'Very good Will!',
	'The Giants suck!',
	'I am the smartest man on earth',
	'Dont\'t worry bud, if the guys are too hard on us, mommy will cuddle us'
]
