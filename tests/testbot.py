import twbotlib

__auth = twbotlib.Auth(
    bot_username='bot_username',
    oauth_token='oauth:token',
)

__bot = twbotlib.Bot(__auth)
__bot.logs = True

async def startup():
    await __bot.join()
    await __bot.wait_until_join()
    await __bot.change_name_color('CadetBlue')

async def command_hello(message):
    await message.channel.send(f'Hello {message.sender}!')

async def command_checkchannel(message):
    await message.channel.send(f'#{message.channel}')

async def command_checkrepr(message):
    await message.channel.send('Checked.')

if __bot.connect():
    print('Bot connected successfully.')

    __bot.read_commands(globals())
    __bot.run(startup)
else:
    print('Something is wrong... Connection failed.')
