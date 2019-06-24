import json

from YahooWeather import response

output = json.loads(response)


class Current:
    city = output['location']['city']
    temp = output['current_observation']['condition']['temperature']
    observation = output['current_observation']['condition']['text']
    sunrise = output['current_observation']['astronomy']['sunrise']
    sunset = output['current_observation']['astronomy']['sunset']
    humidity = output['current_observation']['atmosphere']['humidity']
    visibility = output['current_observation']['atmosphere']['visibility']
    pressure = output['current_observation']['atmosphere']['pressure']
    forecast_next_day = output['forecasts'][0]['day']
    forecast_next_day_high = output['forecasts'][0]['high']
    forecast_next_day_low = output['forecasts'][0]['low']
    forecast_next_day_text = output['forecasts'][0]['text']
    local_conditions = f"The Current Conditions in {city} are, Temperature {temp}F," \
        f" with {observation} conditions"
    sun_conditions = f"Sunrise is at {sunrise} and Sunset is at {sunset}."
    atmospheric_conditions = f"Pressure {pressure} inches, Humidity {humidity}%, Visibility {visibility} miles"
    next_day_forecast = f'The forecast for {forecast_next_day} is a High of {forecast_next_day_high}F,' \
        f' a Low of {forecast_next_day_low}F, and {forecast_next_day_text}...'
