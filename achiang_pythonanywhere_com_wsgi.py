# This file contains the WSGI configuration required to serve up your
# web application at http://achiang.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://www.pythonanywhere.com/wiki/DebuggingImportError


# +++++++++++ HELLO WORLD +++++++++++
# A little pure-wsgi hello world we've cooked up, just
# to prove everything works.  You should delete this
# code to get your own working.


HELLO_WORLD = """
<html>
<head>
    <title>Python Anywhere hosted web application</title>
</head>
<body>
<h1>Hello, World!</h1>
<p>
    This is the default welcome page for a
    <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>
    hosted web application.
</p>
<p>
    Find out more about how to configure your own web application
    by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
</p>
</body>
</html>"""

from datetime import datetime

#HELLO_WORLD += " the time is {}".format(datetime.now())

#def application(environ, start_response):
#    if environ.get('PATH_INFO') == '/':
#        status = '200 OK'
#        content = HELLO_WORLD
#    else:
#        status = '404 NOT FOUND'
#        content = 'Page not found.'
#    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
#    start_response(status, response_headers)
#    yield content.encode('utf8')


from cgi import parse_qs, escape

def application(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))

    if 'url' in parameters:
        url = escape(parameters['url'][0])
    else:
        url = 'www.google.com'
##################################
    url_data = getdata(url)
    helloworld = "<html><head><title>Python Anywhere hosted web application</title></head><body><h1>Hello, "
    helloworld +=  url_data + "!</h1></body></html>"

    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(helloworld)))]
    start_response(status, response_headers)
    yield helloworld.encode('utf8')

#

from bs4 import BeautifulSoup

import requests

def getdata(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    alink = soup.find('a')
    return(alink.get('href'))


