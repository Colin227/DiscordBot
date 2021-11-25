import config 
import discord
import getMessage
import stockTracker


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
    
    # All commands start with an exclamation point, and the proceeding text differentiates between them
    if message.content.startswith('!'):
        #await message.channel.send(file=discord.File('./img/goodnight.mp4'))
        # Assign the command and usernames to variables -- not entirely necessary - could pass message object directly
        msg = message.content
        usr = message.author.display_name

        # build the bot message wiht the getMessage handler, then send it to discord server
        botMessage = getMessage.getCommand(msg, usr, message.author)
        await message.channel.send(botMessage)

    if message.content.startswith("$"):
        botMessage = stockTracker.getStockPrice(message.content)
        if str(botMessage).endswith('.gif'):
            await message.channel.send(file=discord.File(botMessage))
        else:
            await message.channel.send(botMessage)
client.run(config.api_token)