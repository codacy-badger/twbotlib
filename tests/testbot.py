from random import randint
import twbotlib

__auth = twbotlib.Auth(
    bot_username='bot_username',
    oauth_token='oauth:token',
    channel_name='bot_username'
)

__bot = twbotlib.Bot(__auth)
__bot.logs = True

async def startup():
    await __bot.join()
    await __bot.wait_until_join()
    await __bot.change_name_color('CadetBlue')

async def __command_roll(message, args:list=None):
    if args and int(args[0]) < 101:
        await message.channel.send(randint(1, int(args[0])))
    else:
        await message.channel.send(randint(1, 10))

async def __command_dice(message):
    await __bot.send(f'Cube One: {randint(1, 6)}, Cube Two: {randint(1, 6)}')

async def __command_hello(message):
    await __bot.send(f'Hello {message.sender}!')

async def __command_checkchannel(message):
    await __bot.send(f'#{message.channel}')

async def __command_checkrepr(message):
    print(message)
    await __bot.send('Checked.')

if __bot.connect():
    print('Bot connected successfully.')

    __bot.read_commands(globals())
    __bot.run(startup)
else:
    print('Something is wrong... Connection failed.')
