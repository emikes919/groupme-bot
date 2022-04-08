# groupme-bot

This bot assumes you have a groupme account, have obtained your API key, and are in at least 1 groupme group

Step 1: run groupIDs.py and select the group ID of the group you want to create the bot in

Step 2: set GROUPID to the relevant group ID

Step 3: set the targetUserID to the ID of the person you want the bot to respond to (grab from groupIDs.py json response)

Step 4: name the bot in the bot dict

Step 5: run createBot.py

Step 6: run getBots.py, find the bot you just created,
and enter the bot ID into the botID below

Step 7: commit to git and push to heroku
