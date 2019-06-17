from random import randint
import twbotlib

__auth = twbotlib.Auth(
    bot_username='bot_username',
    oauth_token='oauth:token'
)

__bot = twbotlib.Bot(__auth)

def __command_roll(message, args=None):
    if args and int(args) < 101:
        __bot.send(randint(1, int(args)))
    else:
        __bot.send(randint(1, 10))

def __command_dice(message):
    __bot.send(f'Cube One: {randint(1, 6)}, Cube Two: {randint(1, 6)}')

def __command_hello(message):
    __bot.send(f'Hello {message.sender}!')

if __bot.connect():
    print('Bot connected successfully.')

    __bot.read_commands(globals())
    __bot.wait_until_join()
    __bot.run()
else:
    print('Something is wrong... Connection failed.')
