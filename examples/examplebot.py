import twbotlib

auth = twbotlib.Auth(
    bot_username='bot_username',
    oauth_token='oauth:token',
)

bot = twbotlib.Bot(
    auth
)

async def startup():
    await bot.join()

async def __command_hello(message):
    await message.channel.send('Hello, World!')

if bot.connect():
    print('Connected.')
    bot.read_commands(globals())
    bot.run(startup)
