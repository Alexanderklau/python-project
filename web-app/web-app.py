import urllib.request
from urllib.request import urlparse
LOGIN = 'wesc'
PASSID = "you'11NeverGuess"
URL = 'http://localhost'

def handler_version(url):
    from urllib.request import urlparse as up
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password('Archives',up(url)[1],LOGIN,PASSID)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url

def request_varsion(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN,PASSID))[:-1]
    req.add_header("Authorization","Basic %s" % b64str)
    return req

for funcType in ('handler','request'):
    print('*** Using %s:' % funcType.upper())
    url = eval('%s _version')(URL)
    f = urllib.request.urlopen(url)
    print(f.readline())
    f.close()