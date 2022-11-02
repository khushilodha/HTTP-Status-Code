# import request from urllib
# resp = request.urlopen("https://www.wikipedia.org")
# type(resp)

# import requests
# r = requests.get("https://www.youtube.com/")
# print(r.status_code)

import requests as req
import argparse
from logging import exception
parser = argparse.ArgumentParser()
# r = requests.get('https://www.wikipedia.org')
try:
    parser.add_argument('-u', '--url', type=str, required=True)
    parser.add_argument('-f','--fname',type=str, required=True)

    args = parser.parse_args() #constructor
    url=args.url
    print(url)

    r= req.get(url)
    print(r.status_code)
    print(r.text)
 
    fname=args.fname
    f1= open(fname, 'w')
    f1.write(r.text)

except Exception as e:
    print(e)

# from ast import arg
# import sys
# arg= sys.argv
# r='https://www.wikipedia.org'
# if arg.request == 'https://www.wikipedia.org':
#     print(r.status_code)
# else:
#     print('Invalid URL'

