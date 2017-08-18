#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import watcher

class BezrealitkyWatcher(watcher.Watcher):

	def __init__(self):
		self.name = "bezrealitky"

	def _itemText(self,a):	
		return a["title"].encode('utf-8')+" "+str(a["price"])+"kc "\
		"- "+time.strftime("%a, %d %b %H:%M:%S",time.localtime(a["time_order"]))

	def _itemUrl(self,a):
		return "https://www.bezrealitky.cz/nemovitosti-byty-domy/"+str(a["id"])


	def getItems(self):
		data = self.getJSON()
		if not "squares" in data or len(data['squares']) == 0:
			return []	

		return data['squares'][0]['records']
		

	def getSubject(self,item):
		return "Bezrealitky alert: " + self._itemText(item)

	def getBody(self,item):
		text = "Hey!\n" + \
		"New reality on Bezrealitky.cz added.\n" + \
		self._itemText(item) + "\n" + self._itemUrl(item) + "\n\n"
		
		return text	

	def getID(self,item):
		return item['id']



