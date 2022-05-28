# groupme-bot

This bot assumes you have a groupme account, have obtained your API key, and are in at least 1 groupme group. It also requires that you have a basic heroku app set up which you can use as the bot's callback url.

Before you get started, adjust the message character threshold in row 19 on botAPI.py downward. Currently set to 50K characters, meaning your target will need to send a message at least 50K characters long to trigger the bot. Unless he/she is a very verbose, the bot will never respond!

Step 1: run groupIDs.py and select the group ID of the group you want to create the bot in

Step 2: set GROUPID to the relevant group ID

Step 3: set the targetUserID to the ID of the person you want the bot to respond to (grab from groupIDs.py json response)

Step 4: name the bot in the bot dict

Step 5: run createBot.py

Step 6: run getBots.py, find the bot you just created,
and enter the bot ID into the botID below

Step 7: commit to git and push to heroku

**If you want to delete a bot, run destroyBot.py after entering in the ID of the bot you want to destroy**

See https://dev.groupme.com/docs/v3 for more information
