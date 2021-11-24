import requests
import config

'''
Param: usrDisplayName is the unique user ID for each user in the channel.
This will be compared to the hard coded user ID's, and when matched will 
create a payload object that will contain the weather api key and the users
location, contained in a private config file. These are kept separated to 
hide the user's location and weather api key.

'''

def getWeather(usrDisplayName):
    # Look for username, then assign api key and appropriate location query to payload.
    # Keep api key and location as private in config file.
    match str(usrDisplayName):
        case 'Colin#6399':
            #print("colin case execution")
            payload = {'key': config.weather_api, 'q': config.colin_location}
        case 'Switchshift#2753':
            payload = {'key': config.weather_api, 'q': config.ev_location}
        case 'Mat Langer#4026':
            payload = {'key': config.weather_api, 'q': config.mat_location}
        case 'colin#8308':
            payload = {'key': config.weather_api, 'q': config.ollie_location}
        case _: # default case
            print("default case")
            print(usrDisplayName)
            # Default postal code if no match for user. Default postal code is a familiar area to most members of discord server. 
            # TODO: update this to return error message or other default behaviour.
            payload = {'key': config.weather_api, 'q': 'K0L1L0'} 

    # Make our http request and pass in payload with api key and location information
    # TODO: handle request errors
    r = requests.get('http://api.weatherapi.com/v1/forecast.json', params=payload)
    response = r.json()
    
    # Create formatted string for bot response with current weather and location information
    currentWeather = f'The weather in {response["location"]["name"]} is currently {response["current"]["temp_c"]} degrees celcius.'
    return currentWeather


# Was creating this function to format the weather data and return a string
# Will likely make this function be used for string formatting depending on weather request.
# TODO: Handle all weather string formatting for current weather, forecast weather, and conditions
# Then update getWeather function to respond differently based on weather request 
def prettyWeather(response, usrDisplayName):
    #currentWeather = "The weather in " + response['location'] + " is currently " + response['current']['temp_c']
    currentWeather = f'The weather in {response["location"]["name"]} is currently {response["current"]["temp_c"]}'
    


# Add arguments to dictionary for url
# can change postal code to be for each user
#payload = {'key': config.weather_api, 'q': 'K9H3E4'} 
#r = requests.get('http://api.weatherapi.com/v1/forecast.json?key=b6260ab938fc4466a4033601212411&q=K9H3E4&aqi=no')

# Request weather data based on user location

# print(r.status_code)
# print(r.url)




# print(response['location']['name'])
# print(response['current']['temp_c'])

# print(response['current']['condition']['text'])
# print(response['forecast']['forecastday'][0]['date'])
# print(response['forecast']['forecastday'][0]['day']['maxtemp_c'])
# print(response['forecast']['forecastday'][0]['day']['mintemp_c'])
# print(response['forecast']['forecastday'][0]['day']['condition']['text'])