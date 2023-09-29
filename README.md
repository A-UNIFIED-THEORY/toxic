# Toxic

Toxic is a discord server nuker with a GUI. This is technically just a coding exercise, so if things are buggy let me know.


## Installation

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select New Application, or select an old one if you already tried a bot that said to do this.

![](/images/step1.PNG)

2. Name your application, and agree to the Dev TOS and Dev Policy (even though we both know nobodys reading that)

![](/images/step2.PNG)

3. Go to the "Bot" tab of your application, and press "Add Bot". This will make your nuker a thing.

![](/images/step3.PNG)

4. Your bot should come up, play around with the name and pfp and "General Information" tab. Once done, click "Reset Token", and enter your 2FA code if you have that setup.

![](/images/step4.PNG)

5. Copy your token, i have mine blurred out for privacy reasons. Reminder: NEVER give your bots token or your token to ANYONE, if you dont know the code they will run with it.

![](/images/step5.PNG)

6. Paste your token into the "TOKEN" variable. This is what allows your bot to nuke the server.

![](/images/step6.PNG)

7. Go back to the dev portal, and go to OAuth2 > URL Generator. Click these exact checkmarks. If you dont see them, **look harder**.

![](/images/step7.PNG)
![](/images/step8.PNG)

8. Copy your url, and paste it into your notepad to save for later. Then paste it into BOT_INVITE.

![](/images/step10.PNG)

9. Convince the admins in your server to invite the bot.

![](/images/step11.PNG)

**Congratulations! The bot is now ready to use! Just play with the settings in main.py, and run the code. Your bot should be ready!**


## Decoy/Regular Commands

/ping - Gives the ping of the bot
/kick - Kicks a specified user
/ban - Bans a specified user
/info - Gives information of a user (ID, highest role, date joined, etc.)
/invite - Gives an invite link of the bot
/clear - Clears a certain amount of messages
/help - Shows a list of decoy commands
/create - Creates a channel


## Nuking Commands

nukehelp - Tells you the commands.
dmall - DM's the whole server.
kickall - Kicks the whole server.
banall - Bans the whole server.
nickall - Nicknames the whole server.
admin - Gives you admin.
adminall - Gives the whole server admin.
kaboom - The most important command, deletes all channels and makes more, then pings everyone in those channels.
delroles - Deletes all roles.
delchannels - Deletes all channels.
roles - Deletes all roles, then makes more with a specific name.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## FAQ

Q. Who gave you inspiration for this?

A. **Izzo8#8083.**
    
Q. Should i use an alt?

A. **Yes, i dont want your main banned.**

Q. Is this against the discord TOS?

A. **Yes. You should really only use this if neccesary. Use a VPN if possible too.**

Q. What kind of servers should i nuke with this?

A. **Only servers that are actually doing something bad (ex. proship servers or rcta servers).**
