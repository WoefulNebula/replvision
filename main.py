import disnake
import keepalive
import rpsButton
import os
import random
from disnake.ext import commands
import json

#setup - dont touch
# client = disnake.Client()
client = commands.Bot(command_prefix='v!', case_insensitive = True)
# client = commands.Bot(command_prefix = "v!", description = "Vision Bot", owner_id = 530463618488336403, case_insensitive = True)
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.playing, name = "prefix is v!"))
	print("bot is ready")

#games
@client.command()
async def help(ctx):
	embed = disnake.Embed(title = "Help")
	embed.add_field(name = "Flip", value = "Flips a coin heads or tails", inline=False)
	embed.add_field(name = "Roll", value = "Rolls a dice from 1-6", inline=False)
	embed.add_field(name = "rps", value = "Starts a game of rock paper scissors", inline = False)
	embed.add_field(name = "Vip1", value = "Gives link to private server 1", inline=True)
	embed.add_field(name = "Vip2", value = "Gives link to private server 2", inline=True)
	await ctx.send(embed = embed)

@client.command()
async def flip(ctx):
	if ctx.channel.id == 922681714474618891 or ctx.channel.id == 922959690336460841:
		await ctx.send("This command is disabled in this channel")
		return

	result = random.randrange(0,2)
	
	if result == 0:
		print("tails")
		embed = disnake.Embed(title = "Tails")
		embed.set_image(url = "https://media.discordapp.net/attachments/922673046471467009/925249117704290304/VcoinTails.png?width=465&height=465")
	else:
		print("heads")
		embed = disnake.Embed(title = "Heads")
		embed.set_image(url = "https://media.discordapp.net/attachments/922673046471467009/925249112096538675/VcoinHeads.png?width=465&height=465")
	await ctx.send(embed = embed)

@client.command()
async def roll(ctx):
	if ctx.channel.id == 922681714474618891 or ctx.channel.id == 922959690336460841:
		await ctx.send("This command is disabled in this channel")
		return
		
	result = random.randrange(1,7)
	if(result == 6):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530303781556284/dice_6.png?width=417&height=465"
	elif (result == 5):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530303517327461/dice_5.png?width=417&height=465"
	elif (result == 4):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530303299190804/dice_4.png?width=417&height=465"
	elif (result == 3):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530303114657842/dice_3.png?width=417&height=465"
	elif (result == 2):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530302904954940/dice_2.png?width=417&height=465"
	elif (result == 1):
		url = "https://media.discordapp.net/attachments/922680813588467723/925530302628102144/dice_1.png?width=417&height=465"

	embed = disnake.Embed(title = result)
	embed.set_image(url = url)

	await ctx.send(embed = embed)

@client.command()
async def randomgame(ctx):
	result = random.randrange(0,2)
	if result == 0:
		await ctx.send("Coin")
	else:
		await ctx.send("Dice")

@client.command()
async def rps(ctx, other:disnake.Member):
	if ctx.channel.id == 922681714474618891 or ctx.channel.id == 922959690336460841:
		await ctx.send("This command is disabled in this channel")
		return

	author = ctx.author
	#int(other[3:len(other)-1])
	
	view1 = rpsButton.row_buttons(ctx.author.id)
	await ctx.send(author.mention + "Choose Rock Paper or Scissors", view=view1)

	view2 = rpsButton.row_buttons(other.id)
	await ctx.send(other.mention + "Choose Rock Paper or Scissors", view=view2)

	await view1.wait()
	authorChoice = view1.value
	await view2.wait()
	otherChoice = view2.value

	if authorChoice == otherChoice:
		await ctx.send("**Tie**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
		return
	if authorChoice == 0:
		if otherChoice == 1:
			await ctx.send("**" + other.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
		else:
			await ctx.send("**" + author.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
	elif authorChoice == 1:
		if otherChoice == 0:
			await ctx.send("**" + author.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
		else:
			await ctx.send("**" + other.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
	elif authorChoice == 2:
		if otherChoice == 0:
			await ctx.send("**" + other.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
		else:
			await ctx.send("**" + author.mention +  " Wins!**\n" + author.mention + " picked " + getMove(authorChoice) + "\n" + other.mention + " picked " + getMove(otherChoice))
	
def getMove(value):
	if value == 0:
		return "Rock"
	elif value == 1:
		return "Paper"
	elif value == 2:
		return "Scissors"

@client.command()
async def blackjack(ctx, other:disnake.Member):
	await ctx.send("Coming Soon!")

#util
@client.command()
async def vip1(ctx):
	await ctx.send("https://www.roblox.com/games/379614936?privateServerLinkCode=93919875104130434393771371941146")

@client.command()
async def vip2(ctx):
	await ctx.send("https://www.roblox.com/games/379614936?privateServerLinkCode=93798779146153753504990887689622")

@client.command()
async def values(ctx):
	await ctx.send("http://bit.ly/AssassinValues")

#moderation
@client.command() 
async def timeout(ctx, user:disnake.Member, seconds = 60):
	await user.timeout(duration=seconds)
	await ctx.send("User timedout")

#fees
 
@client.command()
async def log(ctx, value):
# user check
	userID = ctx.author.id
	isMM = False
	print(userID)
	with open('mmfeelog.json') as f:
		data = json.load(f)
	for user in data['users']:
		if user['id'] == userID:
			isMM = True
			print("user found:", user['name'])
			
			#change info
			user['total'] += int(value)
			with open('mmfeelog.json', 'w') as out:
				json.dump(data, out, indent = 4)
			
			#confirmation
			await ctx.send("Welcome "+ user['name'] + ". You haved logged " + value + ", you have a total of "+ str(user['total']) + " logged.")
			embed = disnake.Embed(title = user['name'], description = value + " value logged.\n" + str(user['total']) + " total")
			channel = client.get_channel(922892534928257054)
			await channel.send(embed=embed)
			

	if isMM == False:
		await ctx.send("You are not a MM.")
	
	await ctx.message.delete()
	print("isMM: ", isMM)

@client.command()
async def reset(ctx):
	author = ctx.author.id
	if author != 248872936159707137 and author != 820741900293898340 and author != 530463618488336403:
		await ctx.send("You are not authorized to do that!")
	else:
		confirmation = ctx.send("Are you sure you want to do this?")
		await confirmation.add_reaction("👍")
		await client.wait_for("reaction", timeout=30)
		#open file
		with open('mmfeelog.json') as f:
			data = json.load(f)
		#reset totals
		for user in data["users"]:
			user["total"] = 0
		#dump file
		with open('mmfeelog.json', 'w') as out:
			json.dump(data, out, indent = 4)
		await ctx.send("Fee totals reset")

@client.command()
async def fees(ctx):
	authorized = False
	for role in ctx.author.roles:
		if role.id == 922883634652934204 or role.id == 922677079953256448:
			authorized = True
	if authorized == False:
		await ctx.send("You are not authorized to do that!")
		return
	embed = disnake.Embed(title = "Fees")
	embed.set_footer(text="v!reset to reset")
	with open('mmfeelog.json') as f:
			data = json.load(f)
	for user in data["users"]:
		embed.add_field(name=user["name"], value=str(user["total"])+ " value", inline=True)

	await ctx.send(embed=embed)

token = os.getenv("TOKEN")
keepalive.keep_alive()
client.run(token)