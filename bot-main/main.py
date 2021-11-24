import config 
import discord
import getMessage


from datetime import date

# This is a discord bot that will respond to chat messages
# It will be based off the robot Bender from the TV show Futurama

# instantiate the client instance
client = discord.Client()


# Print that bot had successful log in
# Set bot activity status to a quote from bender
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('Bite my shiny metal ass'))

# Listen for messages from discord users
# If message is from the bot, ignore the message.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # goodnight Mat 
    if message.content.startswith('!'): # change to if message starts with '!'
        #await message.channel.send(file=discord.File('./img/goodnight.mp4'))
        msg = message.content
        usr = message.author.display_name
        botMessage = getMessage.getCommand(msg, usr, message.author)
        await message.channel.send(botMessage)

# function that returns a string of the command
# match case statement


client.run(config.api_token)