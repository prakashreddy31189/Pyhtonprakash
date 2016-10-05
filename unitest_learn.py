import unittest

class Test_1(unittest.TestCase):
	def test_add(self):
		self.assertEqual(1+1, 2)


if __name__== '__main__':
	unittest.main()


#print dir(unittest.TestCase)