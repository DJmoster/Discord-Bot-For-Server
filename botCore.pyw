# Autistic Gaming Helper [BOT]

import json 
import discord
import random

from botConfig import BOT_DISCORD_TOKEN, DISCORD_CHANNEL_ID


class bot_Main():

    def __init__(self):
        self.client = discord.Client()


        @self.client.event
        async def on_message(message):

            if message.content.startswith('-help'):

                embed = discord.Embed(title='Команди бота:', color=0x00FF00)
                embed.add_field(name='**-roll**', value='Рандомне число від 0 до 100')

                await message.channel.send(embed=embed)
                await message.delete()


            if message.content.startswith('-roll'):
                author = str(message.author)
                author = str(author[ : author.find('#') ])

                await message.channel.send('@{0} ти зароляв число: {1}'.format(author, str(random.randrange(0,100))))
                await message.delete()


            if message.content.startswith('-log'):
                log_message = str(message.content)
                log_message = str(str(message.author) + ' ' + log_message[ log_message.find(' ') : ])

                channel = self.client.get_channel(DISCORD_CHANNEL_ID)

                await channel.send(log_message)


        self.client.run(BOT_DISCORD_TOKEN)
        

bot_Main()



# embed.add_field(name='', value='')