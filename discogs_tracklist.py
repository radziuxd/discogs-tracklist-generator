#Discogs Tracklist-Tool
#Author: Fabian Baumanis
#Version: 0.1
#Description: Fetches the Tracklist of
#!/usr/bin.env/python

from lxml import html
import requests

#load page
page = input("Please enter the link to the release: ")
source = requests.get(page)
tree = html.fromstring(source.content)

#get the tracklist
tracklist = tree.xpath('//span[@itemprop="name"]/text()')

#print tracklist
for item in tracklist:
    print(item)
