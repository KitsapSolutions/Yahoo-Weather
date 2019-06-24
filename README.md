# Yahoo-Weather
A weather API script updated for Python 3.

You will need to sign up for Yahoo at https://developer.yahoo.com/.

Create an app at https://developer.yahoo.com/apps/.

Documentation at https://developer.yahoo.com/weather/documentation.html.

Enter your app_id, consumer_key, and consumer_secret as indicated.

Change LOCATION as required.

run "python Weather.py LOCATION"

Output should be a JSON object by default. Change the "format: json" to suit your needs.

Changes were required due to the Python HMAC implementation requiring encoding and subsequent decoding.
