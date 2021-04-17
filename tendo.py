import discord

import random
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv('.env')

client = commands.Bot(command_prefix = "p.",
                      case_insensitive = True,
                      activity = discord.Game(name = 'with the knvies!'),
                      status = discord.Status.online
                      )
client.remove_command('help')

@client.event
async def on_ready():
    print('Tendo has started sharpening the knives.')

@client.command()
async def die(ctx):
    if ctx.author.id in [436973854485643264]:
        await ctx.send(f"Bye Daddy {ctx.author.display_name}!")
        await client.logout()

@client.command()
async def ping(ctx):
    await ctx.send(f'...you little- *robot mode* ``The Ping is {round(client.latency * 1000)}ms``')

@client.command()
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'Hell yeah!',
                'Without a doubt.',
                'Yes – definitely.',
                'Of course you dumb dumb.',
                'As I see it, yes.',
                'Most likely.',
                'Yeah pretty much.',
                'Daddy Mizu says yes!',
                'The council says yes.',
                'Uhhhhhhhhh.',
                'I will tell you later.',
                'Better not tell you now.',
                'It is a secret.',
                'Wait till your birthday for an answer.',
                'Eh...no.',
                'Nu!.',
                'Daddy Mizu says nu!',
                'Of course not.',
                'Very doubtful.']
    await ctx.send(f":8ball: **{ctx.author.name}'s Question:** *{question}*\n:8ball: **My wisdom:** *{random.choice(responses)}*.")

@client.command()
async def whoisToru(ctx):
    await ctx.send('Ask Toru')

@client.command()
async def americaisbest(ctx):
    await ctx.send('https://youtu.be/IdKm5lBb2ek?t=118 911 tho...its the best bro :knife:')

@client.command()
async def marryme(ctx):
    await ctx.send('*ignores and walks away...comes back with a 5ft knife*.')

@client.command()
async def loli(ctx):
    await ctx.send('Even I have high enough standards to not murder lolis...unless')

@client.command()
async def cookie(ctx):
    await ctx.send('No frick off my cookie.')

@client.command()
async def milk(ctx):
    await ctx.send('*snatches gallon and chugs*')

@client.command()
async def dice(ctx):
    responses = ['1',
                '2',
                '3',
                '4',
                '5',
                '6']
    await ctx.send(f':handshake: *rolling the dice* \n\n:game_die: You rolled a {random.choice(responses)}')

@client.command()
async def jam(ctx):
    await ctx.send('*jams alone under the rain in the middle of the night*')

@client.command()
async def back(ctx):
    await ctx.send('*Tendo has gotten the milk ~~for himself~~*')

#Tendo's Special Commands

@client.command()
async def hug(ctx, member: discord.Member):
    link = ['https://tenor.com/view/teria-wang-kishuku-gakkou-no-juliet-hug-anime-gif-16509980',
            'https://tenor.com/view/anime-hug-sweet-love-gif-14246498',
            'https://tenor.com/view/gravity-falls-tactical-hug-emergency-hug-hug-hugging-gif-4451990',
            'https://tenor.com/view/puuung-puung-love-you-hug-comfort-gif-13883173',
            'https://tenor.com/view/anime-choke-hug-too-tight-gif-14108949',
            'https://tenor.com/view/hug-anime-sweet-gif-10195705']

    await ctx.send(f'*{ctx.author.name} hugged {member.mention}*...ew \n{random.choice(link)}')

@client.command()
async def smack(ctx, member: discord.Member):
    link = ['https://tenor.com/view/chikku-neesan-girl-hit-wall-stfu-anime-girl-smack-gif-17078255',
            'https://media.discordapp.net/attachments/706514546432540682/761841388580372510/tenor.gif',
            'https://discord.com/channels/705775844811079680/707470040978685962/767698450983682049',
            'https://tenor.com/view/slap-handa-seishuu-naru-kotoishi-barakamon-anime-barakamon-gif-5509136',
            'https://images-ext-1.discordapp.net/external/PTu9TahlTEaW9ppqMriRgas0bC6zVSIrkIteZy9X13w/https/cdn.weeb.sh/images/HkJ6-e91z.gif',
            'https://images-ext-2.discordapp.net/external/qA7fZdO8BpoYMxczVEhoaCjmQeccYMHYsA0rckBGLGE/https/cdn.weeb.sh/images/H1n57yYP-.gif']

    await ctx.send(f'*{ctx.author.name} smacked {member.mention}* **D I S C O M B O B U L A T E** \n{random.choice(link)}')

@client.command()
async def abort(ctx, member: discord.Member):
    abortnum = random.randint(1, 11)

    abortran = discord.Embed(
        title='Abortion <:Thonk:792322336149078017>',
        description=f'If I had to say /10 how bad {member.mention} has to be aborted I would say... **{abortnum}/10**',
        colour = discord.Colour(0Xb8f2f2)
    )

    abortran = await ctx.send(embed = abortran)


client.run(os.getenv('DISCORD_TOKEN'))
