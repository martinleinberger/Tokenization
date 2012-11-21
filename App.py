__author__ = 'martin'

import sys
import getopt
import json
import Tokenization

# ----------- command line parsing --------------
inputFile  = './input/Cut.java.tokens.json'
outputFile = './results.json'

opts, args = getopt.getopt(sys.argv[1:], 'hi:o:')
for opt, arg in opts:
	if opt == '-h':
		print 'App.py -i <inputFile> -o outputFile'
		sys.exit()
	elif opt in ['-i', '-ifile']:
		inputFile = arg
	elif opt in ['-o', '-ofile']:
		outputFile = arg
# ------------------------------------------------

tokens = json.load(open(inputFile))
result = []
for token in tokens:
	if token['class'] == 'kw' or token['class'] == 'de' or token['class'] == 'me':
		result += []

print json.dumps(result)
open(outputFile, 'w').write(json.dumps(result))