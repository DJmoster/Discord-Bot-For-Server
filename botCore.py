# Autistic Gaming Helper [BOT]

import json 
import discord

from discord.ext import commands



class bot_main():

    def get_data_from_file(self):
        with open('bot_data.json', 'r') as F:
            data = json.load(F)
            F.close()
        
        return data


    def __init__(self):
        bot  = commands.Bot(command_prefix='!')
        data = self.get_data_from_file()

        @bot.event
        async def on_ready():
            print('Logged in as')
            print(bot.user.name)
            print(bot.user.id)
            print('------')

        @bot.command(pass_context=True)
        async def test(ctx):
            await ctx.send('OK') 



        bot.run(data['BOT_TOKEN'])


bot_main()