import unittest
import logging, sys, os
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

class TestXPathValid(unittest.TestCase):

    def setUp(self) -> None:
        logging.info("Logger initialized ! ")

    #@unittest.skip("xpath validation skipped")
    def test_edamxpathvalidator(self):
        process = subprocess.run(['edamxpathvalidator', '../../edamontology/EDAM_dev.owl'], env=os.environ.copy())
        self.assertEqual(process.stdout,'')
        self.assertEqual(process.stderr,'')
        if process.returncode != 0:
            self.fail(f'edamxpathvalidator failed with rc {process.returncode}')
            
    def tearDown(self) -> None:
        logging.info("End of unit test")


if __name__ == '__main__':
    unittest.main()
