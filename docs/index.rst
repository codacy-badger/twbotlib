**********************
Twbotlib Documentation
**********************

*******************************************
Create your first twitch bot using twbotlib
*******************************************

| First of all, create new Python file. For example we call it "bot.py".
| Then import twbotlib like that:

.. code-block:: python

    import twbotlib

| Now we need to set an auth variable for the twitch bot parameters (as: bot_username, oauth_token...).
| We need to provide into Auth minimum the bot_username and the oauth_token kwarguments.
| Bot_username is the username of the user that you want to use as your twitch bot.
| Oauth_token is the oauth token that you can receive here: https://twitchapps.com/tmi/.
| You can see how to set the Auth below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )

