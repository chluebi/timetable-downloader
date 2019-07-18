import discord
import main
import json


with open('config.json', 'r') as f:
    config = json.load(f)

client = discord.Client()
c = config['discord']['client-id']
invite = f'https://discordapp.com/oauth2/authorize?client_id={c}&scope=bot&permissions=35840'


@client.event
async def on_ready():
    print('----- bot is ready -----')
    print('invite link:')
    print(invite)


@client.event
async def on_message(message):
    if message.content.startswith('-timetable'):
        await message.add_reaction('✔')
        await main.make_timetable(config)
        with open('cut_timetable.png', 'rb') as f:
            await message.channel.send(file=discord.File(f))

client.run(config['discord']['secret'])
