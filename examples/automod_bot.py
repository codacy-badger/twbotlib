from random import choice
import twbotlib

auth = twbotlib.Auth(
    bot_username='bot_username',
    oauth_token='oauth:token',
)

bot = twbotlib.Bot(
    auth,
    prefix='..',
)

bad_words = ['bad', 'words']

async def startup():
    await bot.join()

async def on_message(message):
    for word in bad_words:
        if word in message.content:
            await bot.timeout(message.sender)
            await message.channel.send(f'{message.sender} was timeouted for 10 minutes (reason: bad word).')
            break

async def command_color(message):
    color_var = choice(twbotlib.colors)

    await bot.change_name_color(
        color_var
    )

    await message.channel.send(
        f'Name color changed to {color_var}.'
    )

if bot.connect():
    bot.event.on_message = on_message
    bot.read_commands(globals())
    bot.run(startup)
