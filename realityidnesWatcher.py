#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import watcher

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


class RealityidnesWatcher(watcher.Watcher):

	def __init__(self):
		self.name = "realityidnes"


	def getItems(self):
		html = self.getHTML()
		a = html.body.find(attrs={'id':'listingRealty'})
		b = a.findChildren(attrs={'class':'item'})
		
		c = [{
			'url': x.find('a').get('href').encode('utf-8'),
			'title': x.find('a').text.encode('utf-8'),
			'text': x.find(attrs={'class':'text'}).text.encode('utf-8'),
			'price': x.find(attrs={'class':'price'}).text.encode('utf-8').replace('&nbsp;',' ')
		} for x in b]
		
		return c

	def getSubject(self,item):
		ret = "Idnes alert: " + item['title']
		#print ret
		#print type(ret)
		#ret = ret.encode('utf-8')
		#print type(ret)
		return ret

	def getBody(self,item):	
		text = "Price: " + item['price'] + "\n\n" + \
		"Hey!\n" + \
		"New reality on reality.idnes.cz added.\n\n" + \
		item['text'] + "\n" + \
		"http://reality.idnes.cz" + item['url'] + "\n\n"
		return text	

	def getID(self,item):
		return item['url']



