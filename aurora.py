import discord
import requests

# Bot token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# WeatherAPI URL
API_KEY = 'YOUR_WEATHER_API_TOKEN'
WEATHER_URL = 'http://api.weatherapi.com/v1/current.json'

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')  # Log the received message

        # Respond to the command !hello
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')  # Simple response

        # Respond to the command !rec [city]
        elif message.content.startswith('!rec'):
            city = message.content.split(' ')[1] if len(message.content.split(' ')) > 1 else None
            if city:
                weather_data = get_weather(city)
                if weather_data:
                    recommendation = make_recommendation(weather_data)
                    await message.channel.send(recommendation)
                else:
                    await message.channel.send('Could not retrieve weather data. Check the city name.')
            else:
                await message.channel.send('Please specify a city. Example: !rec Lisbon')

        # Respond to the command !criteria
        elif message.content.startswith('!criteria'):
            criteria_message = (
                "### Clothing Criteria:\n"
                "**T-shirt:**\n"
                "- Temperature: Above 18°C.\n"
                "- Conditions: Wind below 15 km/h.\n\n"
                "**Hoodie:**\n"
                "- Temperature: Below 18°C or strong wind (above 15 km/h).\n"
                "- Normally worn without a t-shirt underneath, but with a t-shirt underneath in colder temperatures (below 10°C).\n\n"
                "**T-shirt + Hoodie:**\n"
                "- Temperature: Below 10°C, especially if there's wind or rain.\n\n"
                "**Coat:**\n"
                "- Temperature: Below 5°C, especially if there's strong wind or rain.\n\n"
                "**Jeans:**\n"
                "- Temperature: Between 10°C and 20°C.\n"
                "- Conditions: If there is no heavy rain.\n\n"
                "**Track Pants:**\n"
                "- Temperature: Between 5°C and 15°C.\n"
                "- For comfort and mobility in cooler temperatures.\n\n"
                "**Shorts:**\n"
                "- Temperature: Above 20°C.\n"
                "- Conditions: No strong wind and no rain forecast.\n\n"
                "**Umbrella:**\n"
                "- Use: When there is a forecast of rain, regardless of temperature, especially if the feels-like temperature is below 15°C, as the cold and humidity can be uncomfortable."
            )
            await message.channel.send(criteria_message)

        # Respond to the command !why
        elif message.content.startswith('!why'):
            city = message.content.split(' ')[1] if len(message.content.split(' ')) > 1 else None
            if city:
                weather_data = get_weather(city)
                if weather_data:
                    temp = weather_data['temp']
                    wind_speed = weather_data['wind_speed']
                    humidity = weather_data['humidity']
                    await message.channel.send(f"{give_explanation(weather_data)}")
                                               
                else:
                    await message.channel.send('Could not retrieve weather data. Check the city name.')
            else:
                await message.channel.send('Please specify a city. Example: !why Lisbon')

# Function to retrieve weather data from WeatherAPI
def get_weather(city):
    params = {'key': API_KEY, 'q': city}
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            'temp': data['current']['feelslike_c'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
            'precipitation': data['current']['precip_mm']  # Precipitation in millimeters
        }
        return weather_data
    else:
        return None

# Function to make clothing recommendations
def make_recommendation(weather_data):
    temp = weather_data['temp']
    wind_speed = weather_data['wind_speed']
    precipitation = weather_data['precipitation']
    recommendations = []

    # T-shirt
    if temp > 18 and wind_speed < 15:
        recommendations.append("Wear a t-shirt.")
    # Hoodie
    elif temp < 18 or wind_speed > 15:
        if temp < 10:
            recommendations.append("Wear a t-shirt under a hoodie.")
        else:
            recommendations.append("Wear a hoodie.")
    # T-shirt + Hoodie
    if temp < 10 and (wind_speed > 15 or precipitation > 0):
        recommendations.append("Wear a t-shirt and hoodie.")
    # Coat
    if temp < 5 and (wind_speed > 15 or precipitation > 0):
        recommendations.append("Consider wearing a coat.")

    # Pants
    if 10 <= temp <= 20 and precipitation == 0:
        recommendations.append("Wear jeans.")
    elif 5 <= temp < 15:
        recommendations.append("Wear track pants for comfort and mobility.")
    elif temp > 20 and wind_speed < 15 and precipitation == 0:
        recommendations.append("Wear shorts.")
    
    # Umbrella
    if precipitation > 0:
        recommendations.append("Take an umbrella.")

    # Combine recommendations
    if not recommendations:
        recommendations.append("The conditions are good to go without any special clothing.")

    return "\n".join(recommendations)

# Function to provide explanation for the recommendation
def give_explanation(weather_data):
    temp = weather_data['temp']
    wind_speed = weather_data['wind_speed']
    precipitation = weather_data['precipitation']
    humidity = weather_data['humidity']

    explanation = "The recommendations are based on today's data:\n"
    explanation += f"- Feels like temperature: {temp}°C\n"
    explanation += f"- Wind speed: {wind_speed} km/h\n"
    explanation += f"- Precipitation: {precipitation} mm\n"
    explanation += f"- Humidity: {humidity} %\n"

    return explanation

# Configure intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content events

# Initialize the bot client
client = Client(intents=intents)

# Run the bot
client.run(TOKEN)
