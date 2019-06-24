import json

from YahooWeather import response

output = json.loads(response)


class Forecasts:

    for item in output['forecasts']:
        items = json.dumps(item)

    forecast_day_two = output['forecasts'][1]['day']
    forecast_day_two_high = output['forecasts'][1]['high']
    forecast_day_two_low = output['forecasts'][1]['low']
    forecast_day_two_text = output['forecasts'][1]['text']
    day_two = (f"It will be {forecast_day_two_text} on {forecast_day_two} with a high of"
               f" {forecast_day_two_high}F, and a low of {forecast_day_two_low}F")

    forecast_day_three = output['forecasts'][2]['day']
    forecast_day_three_high = output['forecasts'][2]['high']
    forecast_day_three_low = output['forecasts'][2]['low']
    forecast_day_three_text = output['forecasts'][2]['text']
    day_three = (f"It will be {forecast_day_three_text} on {forecast_day_three} with a high of"
                 f" {forecast_day_three_high}F, and a low of {forecast_day_three_low}F")

    forecast_day_four = output['forecasts'][3]['day']
    forecast_day_four_high = output['forecasts'][3]['high']
    forecast_day_four_low = output['forecasts'][3]['low']
    forecast_day_four_text = output['forecasts'][3]['text']
    day_four = (f"It will be {forecast_day_four_text} on {forecast_day_four} with a high of"
                f" {forecast_day_four_high}F, and a low of {forecast_day_four_low}F")

    forecast_day_five = output['forecasts'][4]['day']
    forecast_day_five_high = output['forecasts'][4]['high']
    forecast_day_five_low = output['forecasts'][4]['low']
    forecast_day_five_text = output['forecasts'][4]['text']
    day_five = (f"It will be {forecast_day_five_text} on {forecast_day_five} with a high of"
                f" {forecast_day_five_high}F, and a low of {forecast_day_five_low}F")

    forecast_day_six = output['forecasts'][5]['day']
    forecast_day_six_high = output['forecasts'][5]['high']
    forecast_day_six_low = output['forecasts'][5]['low']
    forecast_day_six_text = output['forecasts'][5]['text']
    day_six = (f"It will be {forecast_day_six_text} on {forecast_day_six} with a high of"
               f" {forecast_day_six_high}F, and a low of {forecast_day_six_low}F")

    forecast_day_seven = output['forecasts'][6]['day']
    forecast_day_seven_high = output['forecasts'][6]['high']
    forecast_day_seven_low = output['forecasts'][6]['low']
    forecast_day_seven_text = output['forecasts'][6]['text']
    day_seven = (f"It will be {forecast_day_seven_text} on {forecast_day_seven} with a high of"
                 f" {forecast_day_seven_high}F, and a low of {forecast_day_seven_low}F")

    forecast_day_eight = output['forecasts'][7]['day']
    forecast_day_eight_high = output['forecasts'][7]['high']
    forecast_day_eight_low = output['forecasts'][7]['low']
    forecast_day_eight_text = output['forecasts'][7]['text']
    day_eight = (f"It will be {forecast_day_eight_text} on {forecast_day_eight} with a high of"
                 f" {forecast_day_eight_high}F, and a low of {forecast_day_eight_low}F")

    forecast_day_nine = output['forecasts'][8]['day']
    forecast_day_nine_high = output['forecasts'][8]['high']
    forecast_day_nine_low = output['forecasts'][8]['low']
    forecast_day_nine_text = output['forecasts'][8]['text']
    day_nine = (f"It will be {forecast_day_nine_text} on {forecast_day_nine} with a high of"
                f" {forecast_day_nine_high}F, and a low of {forecast_day_nine_low}F")

    forecast_day_ten = output['forecasts'][9]['day']
    forecast_day_ten_high = output['forecasts'][9]['high']
    forecast_day_ten_low = output['forecasts'][9]['low']
    forecast_day_ten_text = output['forecasts'][9]['text']
    day_ten = (f"It will be {forecast_day_ten_text} on {forecast_day_ten} with a high of"
               f" {forecast_day_ten_high}F, and a low of {forecast_day_ten_low}F")
