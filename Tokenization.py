__author__ = 'martin'

import sys
import json
import getopt


# Problematic getSubDepts
# because "gets" is a perfectly fine word => [gets, ubdepts]


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


def greedyTokens(start, t, oracle):
	if t == 'LinkedList':
		print 'test'
	end = len(t)
	if (start == end):
		return []

	while not oracle(t[start:end]):
		end -= 1
		if start == end:
			return [t[start:]]

	return [ t[start:end] ] + greedyTokens(end, t, oracle)

def prepareToken(t):
	return t.lower()

# ----------- command line parsing --------------
inputFile  = './input/Cut.java.tokens.json'
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
	if token['class'] == 'kw' or token['class'] == 'de' or token['class'] == 'me':
		result += [greedyTokens(0, prepareToken(token['text']), oracle)]

print json.dumps(result)
open(outputFile, 'w').write(json.dumps(result))

