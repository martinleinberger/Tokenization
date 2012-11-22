__author__ = 'martin'

import re
import Oracle

# Problematic getSubDepts
# because "gets" is a perfectly fine word => [gets, ubdepts]


def greedy(start, t):
	end = len(t)
	if start == end:
		return []

	while not Oracle.oracle(t[start:end].lower()):
		end -= 1
		if start == end:
			return [t[start:]]

	return [ t[start:end] ] + greedy(end, t)

def refineUnknown(token):
	if not Oracle.oracle(token):
		return greedy(0, token)
	return [ token ]


#difference on splitOnChange and splitPenultimate becomes clear with "isOSGiCompatible"
#try to split on case change - StyledEditorKit => [Styled, Editor, Kit]
def splitOnChange(token):
	boundaries = []
	lastStart = 0
	for idx, char in enumerate(token):
		if char.isupper():
			if idx-1 > 0 and token[idx-1].islower():
				boundaries.append(token[lastStart:idx])
				lastStart = idx

	boundaries.append(token[lastStart:len(token)])
	return boundaries

#try to split one before case changes - HTMLEditor => [HTML, Editor]
def splitPenultimate(token):
	boundaries = []
	lastStart = 0
	for idx, char in enumerate(token):
		if char.isupper():
			if idx+1 < len(token) and token[idx+1].islower():
				if idx-1 > 0:
					boundaries.append(token[lastStart:idx])
					lastStart = idx

	boundaries.append(token[lastStart:len(token)])
	return boundaries

#both methods applied, then it's checked which one provides better results
def splitOnUCLC(token, debug=False):
	refined1 = splitOnChange(token)
	hits1 = 0
	for t in refined1:
		if Oracle.oracle(t.lower()):
			hits1 += 1

	refined2 = splitPenultimate(token)
	hits2 = 0
	for t in refined2:
		if Oracle.oracle(t.lower()):
			hits2 += 1

	if debug:
		print (refined1, hits1)
		print (refined2, hits2)

	if hits2 > hits1:
		return refined2
	return refined1


# buchstabeNummer und NummerBuchstabe fehlen noch
def splitOnSeperators(token):
	return re.split(' _ | \. ', token)

def tokenize(token):
	result = []
	firstStep = splitOnSeperators(token)
	for t1 in firstStep:
		secondStep = splitOnUCLC(t1)
		for t2 in secondStep:
			result += refineUnknown(t2)
	return result