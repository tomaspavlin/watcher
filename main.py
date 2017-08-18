#!/usr/bin/python
# -*- coding: utf-8 -*-

from bezrealitkyWatcher import *
from realityidnesWatcher import *
from ulovdomovWatcher import *

import sys


if len(sys.argv) == 1:
	sys.exit("Help: " + sys.argv[0] + " (all|bezrealitky|realityidnes|ulovdomov) [debug]")

type = sys.argv[1]

debug = (len(sys.argv) > 2 and sys.argv[2] == "debug")

obj = {
	'bezrealitky': BezrealitkyWatcher,
	'realityidnes': RealityidnesWatcher,
	'ulovdomov': UlovDomovWatcher

}

if type == 'all':
	for a in obj:
		print "Processing %s" % a
		obj[a]().run(debug)
elif type in obj:
	obj[type]().run(debug)
else:
	sys.exit("Invalid type")
	

print "Finnished"
