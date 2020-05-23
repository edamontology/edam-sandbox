import unittest
import logging
import sys
import os
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

class TestXPathValid(unittest.TestCase):

    def test_edamxpathvalidator(self):
        edam_path = os.environ.get('EDAM_PATH', 'EDAM_dev.owl')
        process = subprocess.run(['edamxpathvalidator', edam_path], stdout=subprocess.PIPE, universal_newlines=True, env=os.environ.copy())
        self.assertEqual(process.stdout,'', msg=f'Errors detected in the ontology:\n{process.stdout}')
        if process.returncode != 0:
            self.fail(f'edamxpathvalidator failed with rc {process.returncode}')
            
if __name__ == '__main__':
    unittest.main()
