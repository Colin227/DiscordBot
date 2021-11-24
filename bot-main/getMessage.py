import weather
import joke
'''
This is the message handler

It takes in the user message, the nickname being used and the actual username.

We separate the nickname and the username in order to address each user by their
preferred name, while using the username to hard code values that cannot be retrieved
automatically, such as location.

I used match-case in python to direct each command to the proper function.

'''




def getCommand(msg, usr, usrId):
    match msg:
        case '!goodnight':
            #tmpString = "Goodnight " + str(usr).split('#')[0] # was used for retrieving account name without user id #
            tmpString = 'Goodnight ' + str(usr) # Changed to pass nickname to getCommand function now
            return tmpString
        case '!goodmorning':
            # Get current weather info. Pass username as argument which will be used to look up
            # hard coded location information in order to return local weather information.
            currentWeather = weather.getWeather(usrId)
            tmpString = 'Good morning ' + str(usr) + "! " + currentWeather
            return tmpString
        case '!joke':
            tmpJoke = joke.get_joke()
            return tmpJoke
        case _:
            print(msg)
            return "UNKNOWN_COMMAND"