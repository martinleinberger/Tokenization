__author__ = 'martin'

import unittest
import Tokenization

def listCompare(list1, list2):
	if len(list1) == len(list2):
		for i in list1:
			if i not in list2:
				return False
		return True
	return False

class SimpleTest(unittest.TestCase):
	def runTest(self):
		self.assertTrue(listCompare(Tokenization.splitOnUCLC('isOSGiCompatible'), ['is', 'OSGi', 'Compatible']), 'isOSGiCompatible not correctly tokenized')