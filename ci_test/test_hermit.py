import unittest
import logging, sys
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

HERMIT_OK_STRING="Classes equivalent to 'owl:Nothing':\n\towl:Nothing\n"

class TestLogging(unittest.TestCase):

    def setUp(self) -> None:
        logging.info("Logger initialized ! ")

    def test_hermit(self):
        process = subprocess.run(['java', '-jar', 'HermiT.jar', '-U', '../../edamontology/EDAM_dev.owl'], stdout=subprocess.PIPE, universal_newlines=True)
        self.assertEqual(process.stdout, HERMIT_OK_STRING, msg='HermiT reasoner detected some inconsistencies in the ontology')
        if process.returncode != 0:
            self.fail(f'HermiT reasoner failed with rc {process.returncode}')

    def tearDown(self) -> None:
        logging.info("End of unit test")


if __name__ == '__main__':
    unittest.main()
