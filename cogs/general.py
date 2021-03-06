# just gonna make one command and call it a day
import discord 
import platform
import sys
import json
import aiohttp
import random

from discord.ext import commands

class general(commands.Cog):

    def __init__(self, cog):
        self.bot = bot 

    discordpyversion = (discord.__version__)
pythonversion = (platform.python_version())
    
    
class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        embed = discord.Embed(
            description="Hello I Am HimejiBot A general purpose Discord Bot that can server you in several ways c:",
            color=0xE786D7
        )
        embed.add_field(
            name="Author:",
            value="Tylerr#6979",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"[{pythonversion}](https://www.python.org/downloads/release/python-385/)",
            inline=True
        )
        embed.add_field(
            name='Discord.py API Version:',
            value=f"[{discordpyversion}](https://discordpy.readthedocs.io/en/latest/)",
            inline=True
        )
        embed.add_field(
        	name="Prefix:",
            value=f"{config.BOT_PREFIX}",
            inline=True
        )
        embed.add_field(
        	name="Ping/Latency:",
            value=f"{round(self.bot.latency * 1000)} milliseconds",
            inline=True
        )
        embed.set_footer(
            text=f"Requested By {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=0xE786D7
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Owner",
            value=f"{server.owner}\n{server.owner.id}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Member Count",
            value=server.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {time}"
        )
        await context.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, context):
        embed = discord.Embed(
            color=0xE786D7
        )
        embed.add_field(
            name="Pong!",
            value=f":ping_pong:{round(self.bot.latency * 1000)}ms",
            inline=True
        )
        embed.set_footer(
            text=f"Pong request by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, context):
        await context.send("I sent you a private message!")
        await context.author.send(f"Invite me by clicking here: https://discordapp.com/oauth2/authorize?&client_id={config.APPLICATION_ID}&scope=bot&permissions=8")

    @commands.command(name="server")
    async def server(self, context):
        await context.send("I sent you a private message!")
        await context.author.send("Join my discord server by clicking here: https://discord.gg/planets")

    @commands.command(name="poll")
    async def poll(self, context, *args):
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="A new poll has been created!",
            description=f"{poll_title}",
            color=0xE786D7
        )
        embed.set_footer(
            text=f"Poll created by: {context.message.author} • React to vote!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command(name="8ball")
    async def eight_ball(self, context, *args):
        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{answers[random.randint(0, len(answers))]}",
            color=0xE786D7
        )
        embed.set_footer(
            text=f"Question asked by: {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="bitcoin")
    async def bitcoin(self, context):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0xE786D7
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(general(bot))