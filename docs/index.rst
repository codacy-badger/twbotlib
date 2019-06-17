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

| After that we need to assign the main bot variable with our Auth, see below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth)

| Now we need to connect the bot to the twitch IRC. We can check if the connection was successful using the return of the bot "connect" method (On success is returning True, on fail is returning False). See below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth)
    
    if bot.connect():
        print('Bot successfully connected.')
    else:
        print('Bot failed to connect.')

| After we connected successfully, we need wait until the bot joined the channel and then run the bot. See below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth)
    
    if bot.connect():
        print('Bot successfully connected.')
        
        bot.wait_until_join()
        bot.run()
    else:
        print('Bot failed to connect.')

| If we start this script the bot is running!.. but there is no commands. To assign a command we need to create a function with name that starting with "__command_" (for example "__command_hello", to call this command you need to write the query "!hello" or whatever the prefix is.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth)
    
    def __command_hello(message):
        bot.send('Hello!')
    
    if bot.connect():
        print('Bot successfully connected.')
        
        bot.wait_until_join()
        bot.run()
    else:
        print('Bot failed to connect.')

| How we can see, I've added the function "__command_hello", but why I write the "message" argument? because the program is sending this argument on command-function call (This argument is Message object).
| When this command-function is called then is returning "Hello!" in the chat because the "send" method of the bot class is called with the string "Hello!" argument (aka bot.send('Hello!')).
| BUT you already can't call this command. You've just add one line that reading the exist commands by providing the globals() of your file. See below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth)
    
    def __command_hello(message):
        bot.send('Hello!')
    
    if bot.connect():
        print('Bot successfully connected.')
        
        bot.read_commands(globals())
        bot.wait_until_join()
        bot.run()
    else:
        print('Bot failed to connect.')

| And.. That's it!, we add "bot.read_commands(globals())" and now if we run the bot then is full-functional bot that responding on "!hello" command!.
| If you want to change the prefix from "!" to ".." for example then see the code below.

.. code-block:: python

    import twbotlib
    
    auth = twbotlib.Auth(
        bot_username='your_bot_username',
        oauth_token='your_oauth_token'
    )
    
    bot = twbotlib.Bot(auth, '..') # We add more string argument here
    
    def __command_hello(message):
        bot.send('Hello!')
    
    if bot.connect():
        print('Bot successfully connected.')
        
        bot.read_commands(globals())
        bot.wait_until_join()
        bot.run()
    else:
        print('Bot failed to connect.')

| We need just to provide one more string argument! (I comment the line that changed). Now our prefix is ".." then to call a command we need to write "..hello"!.
