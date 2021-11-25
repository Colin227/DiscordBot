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
    
    # Regular commands start with an exclamation point, and the proceeding text differentiates between them
    if message.content.startswith('!'):
        # Assign the command and usernames to variables -- not entirely necessary - could pass message object directly
        msg = message.content
        usr = message.author.display_name

        # build the bot message with the getMessage handler, then send it to discord server
        botMessage = getMessage.getCommand(msg, usr, message.author)
        await message.channel.send(botMessage)

    # Stock commands start with dollar sign. If numbers come after the dollar sign respond with gif instead of stock information
    if message.content.startswith("$"):
        if (message.content.split('$')[1].isdigit()):
            await message.channel.send(file=discord.File('./img/bender-money.gif'))
        else:
            stockDict = stockTracker.getStockPrice(message.content)
            if stockDict == "STOCK_NOT_FOUND":
                await message.channel.send(file=discord.File('./img/bender-broken.gif'))
        # if str(botMessage).endswith('.gif'):
        #     await message.channel.send(file=discord.File(botMessage))
        # else:
            # Build the embedded message
            else:
                embed=discord.Embed(title=stockDict["symbol"], description=stockDict["shortName"], color=0x00947b)
                #embed.set_thumbnail(url=stockDict["logo"])
                embed.add_field(name=f'Current Price: {stockDict["currency"]}', value=f'${stockDict["currentPrice"]}', inline=False)
                embed.add_field(name="Value Change:", value=f'${str(round(stockDict["dollarChange"], 2))}', inline=False)
                embed.add_field(name="Percent Change:", value=f'{str(round(stockDict["percentChange"], 2))}%', inline=False)

                if (stockDict['logo']):
                    embed.set_thumbnail(url=stockDict["logo"])
                    await message.channel.send(embed=embed)
                else:
                    file=discord.File("./img/bender-head.png", filename="bender-head.png")
                    embed.set_thumbnail(url="attachment://bender-head.png")
                    await message.channel.send(file=file, embed=embed)

            
            
        #     print(stockDict["symbol"])
        #     print(stockDict["currentPrice"])
        #     print(stockDict["currency"])
        #     print(stockDict["closePrice"])
        #     print(stockDict["dollarChange"])
        #     print(stockDict["percentChange"])
            #await message.channel.send(botMessage)
client.run(config.api_token)