__author__ = 'martin'

import unittest
import Tokenization

def isEqual(a, b):
	for c in a:
		if c not in b:
			return False
	if not len(a) == len(b):
		return False
	return True

#general test cases
class OSGiTest(unittest.TestCase):
	def runTest(self):
		token = 'isOSGiCompatible'
		expected = ['is', 'OSGi', 'Compatible']
		self.assertTrue(isEqual(Tokenization.tokenize(token), expected), token + ' not correctly tokenized')

class HTMLEditorTest(unittest.TestCase):
	def runTest(self):
		token = 'HTMLEditor'
		expected = ['HTML', 'Editor']
		self.assertTrue(isEqual(Tokenization.tokenize(token), expected), token + ' is not correctly tokenized')

class StyledEditorKitTest(unittest.TestCase):
	def runTest(self):
		token = 'StyledEditorKit'
		expected = ['Styled', 'Editor', 'Kit']
		self.assertTrue(isEqual(Tokenization.tokenize(token), expected), token + ' is not correctly tokenized')

