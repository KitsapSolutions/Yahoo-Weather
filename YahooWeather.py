"""
Weather API Python sample code

Copyright 2019 Oath Inc. Licensed under the terms of the
zLib license see https://opensource.org/licenses/Zlib for terms.

Modified by Kitsap Solutions for use in Python 3.

$ python --version
Python 3.7

"""
import argparse
import time
import uuid
import urllib.request
from urllib.parse import quote
import hmac
import hashlib
from base64 import b64encode
from config import *

config = configparser.ConfigParser()

parser = argparse.ArgumentParser(description='Yahoo Weather API Parser')
parser.set_defaults(format='json')
parser.add_argument('location', help='Location of weather report, CITY, ZIP-CODE')
parser.add_argument('-f', '--forecast', help='Include for forecast only')
# parser.add_argument('-f', '--format', help='Output format, default is json, "xml" for xml')
args = vars(parser.parse_args())


"""
Basic info
"""
url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
app_id = yahoo_app_id
consumer_key = yahoo_consumer_key
consumer_secret = yahoo_consumer_secret
concat = '&'
query = {'location': ('{}'.format(args['location'])), 'format': ('{}'.format(args['format']))}

oauth = {
    'oauth_consumer_key': consumer_key,
    'oauth_signature_method': "HMAC-SHA1",
    'oauth_timestamp': str(int(time.time())),
    'oauth_nonce': uuid.uuid4().hex,
    'oauth_version': '1.0'
}

"""
Prepare signature string (merge all params and SORT them)
"""
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base = (method + concat + urllib.parse.quote(url, safe='')
                  + concat + urllib.parse.quote(concat.join(sorted_params), safe='')).encode('utf-8')

"""
Generate signature
"""

composite_key = (urllib.parse.quote(consumer_secret) + concat).encode('utf-8')
oauth_signature = b64encode(hmac.new(composite_key, signature_base, hashlib.sha1).digest()).decode('utf-8')

"""
Prepare Authorization header
"""
oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ','.join(['{}="{}"'.format(k, v) for k, v in oauth.items()])

"""
Send request
"""
url = url + '?' + urllib.parse.urlencode(query)
request = urllib.request.Request(url)
request.add_header('Authorization', auth_header)
request.add_header('X-Yahoo-App-Id', app_id)
response = urllib.request.urlopen(request).read().decode('utf-8', 'ignore')
