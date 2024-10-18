# Aurora - Discord Weather Bot
This is a Discord bot that provides weather-based clothing recommendations. It uses the WeatherAPI to fetch current weather data and suggests appropriate clothing based on the temperature, wind speed, and precipitation.

## Features

- Provides clothing recommendations based on current weather conditions.
- Explains the rationale behind the recommendations.
- Lists criteria for clothing choices.

## Commands

### `!rec [city]`
Fetches the current weather for the specified city and provides clothing recommendations.

**Example:**

Discord_User: !rec Porto

Aurora_Bot: Wear a t-shirt. Wear shorts.

### `!why [city]`
Explains the reasoning behind the clothing recommendations based on the current weather data.

**Example:**

Discord_User: !why Porto

Aurora_Bot: The recommendations are based on today's data:
- Feels like temperature: 21.4°C
- Wind speed: 5.8 km/h
- Precipitation: 0.0 mm
- Humidity: 69 %

### `!criteria`
Lists the criteria used for making clothing recommendations.

**Example:**

Discord_User: !criteria

Aurora_Bot: Criteria for Recommendations

- **T-shirt**: Above 18°C, wind below 15 km/h.
- **Hoodie**: Below 18°C or strong wind (above 15 km/h).
- **T-shirt + Hoodie**: Below 10°C, especially with wind or rain.
- **Jacket**: Below 5°C, especially with strong wind or rain.
- **Jeans**: Between 10°C and 20°C, no heavy rain.
- **Sweatpants**: Between 5°C and 15°C, for comfort.
- **Shorts**: Above 20°C, no strong wind or rain.
- **Umbrella**: When rain is forecasted, especially if feels like below 15°C.

### Note on `/criteria` Command

The `/criteria` command provides a fixed set of clothing recommendation criteria that are not influenced by the current weather data obtained from the API. This means that regardless of the weather conditions, the output of the `/criteria` command will always remain the same. Additionally, there is no need to specify a city after the `/criteria` command, making it straightforward and easy to use. This ensures users have a consistent reference for understanding the recommendations provided by the bot.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/g0m3s618/Aurora.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd Aurora
   ```
   
3. Install the required packages:
   ```bash
   python3 aurora.py
   ```
4. Replace YOUR_DISCORD_BOT_TOKEN and YOUR_WEATHER_API_TOKEN in the code with your actual Discord bot token and WeatherAPI key.

5. Run the bot:
   ```bash
   python3 aurora.py
   ```
## Useful links
[Discord Developer Portal](https://discord.com/developers/docs/intro)

[WeatherAPI](https://www.weatherapi.com/)
