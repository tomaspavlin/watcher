#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import os.path
import urllib2
import requests
import smtplib
import json

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


from email.mime.text import MIMEText

class Watcher:
	name = ""
	mailfrom = "realitywatcher@prijmeni.cz"
	mailto = "tomas.pavlin@gmail.com"
	# to = "tomas.pavlin@gmail.com,ondrej.basler@gmail.com"


	def __init__(self):
		pass
	def getItems(self):
		raise NotImplementedError()
	def getSubject(self,item):
		raise NotImplementedError()
	def getBody(self,item):
		raise NotImplementedError()
	def getID(self,item):
		raise NotImplementedError()
	
	def run(self,debug=False):		

		fname = self.name+".last"

		#print url

		#print data


		items = self.getItems()

		if len(items) == 0:
			print "Format data error (no items found)"
			return

		if debug:
			for a in items:
				print self.getSubject(a)
			print "==="

		a = self.getItems()[0]

		print self.getSubject(a)

		id = ""
		try:
			with open(fname,"r") as f:
				id = (f.readlines()[0])
		except:
			id = 'magic9692873672893'		

		if id == str(self.getID(a)):
			print "No update"
		else:
			print "New item. Sending mail."
			with open(fname,"w") as f:
				f.write(str(self.getID(a)))
			self._sendMail(a)

	def _sendMail(self,a):

		text = self.getBody(a)
		# Create a text/plain message
		msg = MIMEText(text)

		msg['Subject'] = self.getSubject(a)
		msg['From'] = self.mailfrom
		msg['To'] = self.mailto

		s = smtplib.SMTP('localhost')
		s.sendmail(self.mailfrom, self.mailto.split(","), msg.as_string())
		s.quit()
		return False
	
	def _getURL(self):
		with open(self.name + ".url","r") as f:
			lines = f.readlines()
		url = lines[0].strip()
		return url

	def _getData(self):
		with open(self.name + ".url","r") as f:
			lines = f.readlines()
		
		for url in lines[1:]:
			if url.strip() != "":
				return json.loads(url.strip())
		return {}
	
	def postJSON(self):
		url = self._getURL()
		d = self._getData()
		r = requests.post(url, json=d)
		data = json.loads(r.text)
		return data

	def getJSON(self):
		url = self._getURL()
		response = urllib2.urlopen(url)
		data = json.loads(response.read())
		return data

	def getSource(self):
		url = self._getURL()
		response = urllib2.urlopen(url)
		data = response.read() #json.loads(response.read())
		return data
	
	def getHTML(self):
		return BeautifulSoup(self.getSource())

