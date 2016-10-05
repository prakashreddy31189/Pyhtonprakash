from developed_function import my_contains, my_first
import unittest

class TestMyFunction_1(unittest.TestCase):

	def test_my_contains_function1(self):
		self.assertTrue(my_contains(1, [1,2,3]))

	def test_my_contains_function2(self):
		self.assertTrue(my_contains(2, [1,2,3]))

	def test_my_contains_function3(self):
		self.assertTrue(my_contains(3, [1,2,3]))

	@unittest.expectedFailure
	def test_my_contains_function4(self):
		self.assertTrue(my_contains(4, [1,2,3]))

	@unittest.expectedFailure
	def test_my_contains_function5(self):
		self.assertTrue(my_contains('hi', [1,2,3]))


@unittest.skip('skipping 2nd test')
class TestMyFunction_2(unittest.TestCase):

	def test_first_number1(self):
		self.assertEqual(my_first([1,2,3]), 1)

	@unittest.expectedFailure
	def test_first_number2(self):
		self.assertEqual(2, my_first([1,2,3]), "value not matching")

	@unittest.expectedFailure
	def test_first_number3(self):
		self.assertEqual(my_first([1,2,3]), 3, "value not matching")

	@unittest.expectedFailure
	def test_first_number4(self):
		self.assertEqual(my_first([1,2,3]), "hello", "value not matching")



# Execution Type_1
#if __name__== '__main__':
#	unittest.main(exit=False)

test_suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMyFunction_1)

test_suite2 = unittest.TestLoader().loadTestsFromTestCase(TestMyFunction_2)

all_suite= unittest.TestSuite([test_suite1, test_suite2])

#Execution Type_2(suite1 execution)
#unittest.TextTestRunner(verbosity=2).run(test_suite1)
#unittest.TextTestRunner(verbosity=2).run(test_suite2)


#Execution Type_3(all_suite execution)
unittest.TextTestRunner(verbosity=2).run(all_suite)

print unittest.TestResult()
