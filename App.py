#! /usr/bin/env python
__author__ = 'martin'

import os
import sys
import getopt
import json
import Tokenization


# ----------- command line parsing --------------
#inputFile  = './input/Company.java.tokens.json'
#outputFile = './results.json'

#opts, args = getopt.getopt(sys.argv[1:], 'hi:o:')
#for opt, arg in opts:
#	if opt == '-h':
#		print 'App.py -i <inputFile> -o outputFile'
#		sys.exit()
#	elif opt in ['-i', '-ifile']:
#		inputFile = arg
#	elif opt in ['-o', '-ofile']:
#		outputFile = arg
## ------------------------------------------------



def ignore(file):
	lowered = file.lower()
	for i in ['readme', '101meta', 'org.eclipse.jdt.core.prefs', 'makefile', 'pyjamas']:
		if i in lowered:
			return True

	return False

def walkOverContribution(contributionPath, ignoreFunc = None, endsWith = '.tokens.json'):
	result = {}
	for (path, dirs, files) in os.walk(contributionPath):
		if ignoreFunc(path):
			continue
		for file in files:
			if file.endswith(endsWith):
				if ignoreFunc(file):
					continue
				result[file] = Tokenization.tokenizeFile(os.path.join(path,file))
	return result

cBasePath = '/Daten/101companies/101web/data/resources/contributions'
contributions = os.listdir(cBasePath)


#contributionResults = {}
listOfContribs = []
for contribution in contributions:
	print'processing ' + contribution
	result = walkOverContribution(os.path.join(cBasePath, contribution), ignore)
	if not result == {}:
		listOfContribs.append(contribution)
		open('contributions/' + contribution + '.json', 'w').write(json.dumps(result))

open('contributionsList.json', 'w').write(json.dumps(listOfContribs))


#contributionResults[contribution] = walkOverContribution(os.path.join(cBasePath, contribution), ignore)

#open('full.json', 'w').write(json.dumps(contributionResults))
#print 'finished'
#print contributionResults
