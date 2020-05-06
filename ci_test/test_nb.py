import unittest
import logging, sys

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

class TestNotebooks(unittest.TestCase):

    def setUp(self) -> None:
        logging.info("Logger intialized ! ")

    def test_fail_nb(self):
        try:
            with open('ci_test/failing_nb.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
                print(ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}}))
        except Exception as e:
            message = str(e.args)
            print(message)
            if "sys.exit(ERROR)" in message :
                print('OK')
                pass
            else:
                print('KO')
                self.fail("Error expected")

    def test_warn_nb(self):
        try:
            with open('ci_test/warning_nb.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
                print(ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}}))
        except Exception as e:
            message = str(e.args)
            print(message)
            if "sys.exit(WAR)" in message :
                print('OK')
                pass
            else:
                print('KO')
                self.fail("Warning expected")

    def tearDown(self) -> None:
        logging.info("End of unit test")


if __name__ == '__main__':
    unittest.main()
