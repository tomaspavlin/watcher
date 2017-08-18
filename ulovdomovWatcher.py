#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import watcher

class UlovDomovWatcher(watcher.Watcher):

	def __init__(self):
		self.name = "ulovdomov"

	def _itemText(self,a):	
		return str(a["price_rental"])+"kc " + a['seo'].encode('utf-8')

	def _itemUrl(self,a):
		return a["absolute_url"]


	def getItems(self):
		data = self.postJSON()
		if not "offers" in data or len(data['offers']) == 0:
			return []	

		return data['offers']
		

	def getSubject(self,item):
		return "UlovDomov alert: " + self._itemText(item)

	def getBody(self,item):
		a = ""#item["description"].decode().encode('utf-8') 
		b =  self._itemUrl(item) 

		text = "Hey!\n" + \
		"New reality on UlovDomov.cz added.\n" + \
		a + "\n" + b + "\n\n"
		
		return text	

	def getID(self,item):
		return item['id']



