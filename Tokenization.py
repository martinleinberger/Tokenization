__author__ = 'martin'

import sys
import json
import getopt


# Problematic ALTORENDSTATE
# because "alto" is a perfectly fine word


def loadList(fileName):
	list = []
	file = open(fileName)
	line = file.readline().replace('\n', '')

	while line:
		list.append(unicode(line))
		line = file.readline().replace('\n', '')
	file.close()
	return list

wordList = loadList('english-words.10')
wordList += loadList('english-words.20')

def oracle(term):
	return (term in wordList)


def refineTokens(start, t, oracle):
	if t == 'LinkedList':
		print 'test'
	end = len(t)
	if (start == end):
		return []

	while not oracle(t[start:end]):
		end -= 1
		if start == end:
			return [t[start:]]

	return [ t[start:end] ] + refineTokens(end, t, oracle)

def prepareToken(t):
	return t.lower()

# ----------- command line parsing --------------
inputFile  = './Company.java.tokens.json'
outputFile = './results.json'

opts, args = getopt.getopt(sys.argv[1:], 'hi:o:')
for opt, arg in opts:
	if opt == '-h':
		print 'Tokenization.py -i <inputFile> -o outputFile'
		sys.exit()
	elif opt in ['-i', '-ifile']:
		inputFile = arg
	elif opt in ['-o', '-ofile']:
		outputFile = arg
# ------------------------------------------------

tokens = json.load(open(inputFile))
result = []
for token in tokens:
	if token['class'] == 'kw' or token['class'] == 'de':
		result += [refineTokens(0, prepareToken(token['text']), oracle)]

print json.dumps(result)
open(outputFile, 'w').write(json.dumps(result))

