# Autistic Gaming Helper [BOT]

import json 
import discord
import random

from botConfig import BOT_TOKEN


class bot_Main():

    def __init__(self):
        self.client = discord.Client()

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return 0
            
            if message.content.startswith('-help'):

                embed = discord.Embed(title='Команди бота:', color=0x00FF00)
                embed.add_field(name='**-roll**', value='Рандомне число від 0 до 100')


                await message.channel.send(embed=embed)

            if message.content.startswith('-roll'):
                await message.channel.send('Число: {0}'.format(str(random.randrange(0,100))))


        self.client.run(BOT_TOKEN)

bot_Main()



# embed.add_field(name='', value='')