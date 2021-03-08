import unittest
import HtmlTestRunner
import tests.lib.utils
import tests.lib.Base


from datetime import datetime

folder_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# test_suite = unittest.defaultTestLoader.discover(start_dir='./tests', pattern='*Test.py')
# test_suite = unittest.defaultTestLoader.discover(start_dir='./tests', pattern='OperationsReport*Test.py')
test_suite = unittest.defaultTestLoader.discover(start_dir='./tests', pattern='WeightWatchers_Test.py')

# runner = unittest.TextTestRunner(verbosity=2)
runner = HtmlTestRunner.HTMLTestRunner(output=folder_name, combine_reports=True, report_name="PlaytestReport", add_timestamp=True)
runner.run(test_suite)
