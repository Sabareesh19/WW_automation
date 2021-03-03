
import unittest

class TestSuiteExtensions():
    @staticmethod
    def suite_from_testnames(test_class, test_names=[]):
        # Run a specific test in a class
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(test_class(name))
        return suite

    @staticmethod
    def suite_from_testclass(test_class):
        # Run the tests in a specific class
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        return suite

    @staticmethod
    def suite_from_testclasses(testclasses_list):
        # Run only the tests in the list of specified classes
        suites_list = []
        for test_class in testclasses_list:
            suite = TestSuiteExtensions.suite_from_testclass(test_class)
            suites_list.append(suite)
        return unittest.TestSuite(suites_list)