import unittest
import logging
import os
import sys
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

HERMIT_OK_STRING="Classes equivalent to 'owl:Nothing':\n\towl:Nothing\n"

class TestLogging(unittest.TestCase):

    def test_hermit(self):
        edam_path = os.environ.get('EDAM_PATH', 'EDAM_dev.owl')
        process = subprocess.run(['java', '-jar', 'HermiT.jar', '-U', edam_path], stdout=subprocess.PIPE, universal_newlines=True)
        self.assertEqual(process.stdout, HERMIT_OK_STRING, msg='HermiT reasoner detected some inconsistencies in the ontology')
        if process.returncode != 0:
            self.fail(f'HermiT reasoner failed with rc {process.returncode}')

if __name__ == '__main__':
    unittest.main()
