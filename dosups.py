#!/usr/bin/env python

import requests
from HTMLParser import HTMLParser
import time
import sys

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            print attrs[0][1]

    # def handle_endtag(self, tag):
    #     print "Encountered an end tag :", tag
    #
    # def handle_data(self, data):
    #     print "Encountered some data  :", data

pattern = "https://www.thegazette.co.uk/London/issue/"

print 'supplement,date'

for i in range(1,62045):
    url = pattern + str(i) + '/supplement'
    # print url
    r = requests.get(url)
    if r.status_code == 404:
	continue
    parser = MyHTMLParser()
    sys.stdout.write(str(i) + ',') 
    parser.feed(r.text)
    time.sleep(1)
