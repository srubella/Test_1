import unittest
import unittestsample

class TestMain(unittest.TestCase):
	def dostuff(self):
		x = 10
		result = unittestsample.addition(x)
		self.assertequal(result,20)

	def dostuff1(self):
		x = 'dfd'
		result = unittestsample.addition(x)
		self.assertequal(result,20)

if __name__=='__main__':
	unittest.main()

