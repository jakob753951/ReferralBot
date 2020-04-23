import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from configuration import configuration, load_config


cfg = load_config('config.json')

bot = commands.Bot(command_prefix=commands.when_mentioned_or(cfg.prefix), description=cfg.description, pm_help=True)


def log(message):
	print(f'{str(datetime.now())[:-7]}: {message}', flush=True)

@bot.event
async def on_ready():
	log('Connected!')
	log(f'Username: {bot.user.name}')
	log(f'ID: {bot.user.id}')

@bot.event
async def on_message_edit(before, after):
	if not after.channel.guild:
		log(f'Direct message>{str(after.author)}: "{before.content}" --> "{after.content}"')
	else:
		log(f'{str(after.server)}>{str(after.channel)}>{str(after.author)}: "{before.content}" --> "{after.content}"')

@bot.event
async def on_message(message):
	if message.author != bot.user:
		if not message.channel.guild:
			log(f'Direct message>{str(message.author)}: "{message.content}"')
		else:
			log(f'{str(message.guild)}>{str(message.channel)}>{str(message.author)}: "{message.content}"')
	await bot.process_commands(message)

@bot.command()
async def referrals(ctx):
	d = {}
	invites = await ctx.guild.invites()

	for invite in invites:
		if invite.inviter not in d:
			d[invite.inviter] = 0
		
		d[invite.inviter] += invite.uses
	
	for user, referrals in d.items():
		await ctx.send(f'{user.mention}: {referrals}')

bot.run(cfg.token)