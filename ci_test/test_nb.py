import unittest
import logging, sys
from parameterized import parameterized
import glob
import os
import json

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', stream=sys.stdout)

class TestNotebooks(unittest.TestCase):


    def setUp(self) -> None:
        logging.info("Logger intialized ! ")

    def test_output_nb(self):
        with open('ci_test/RaisingExceptions.ipynb') as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True)
            ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}})

            edam_test_output = nb['cells'][-1]['outputs'][0]['text']
            out = json.loads(edam_test_output)
            print()
            print(f"test name: {out['test_name']}\nstatus: {out['status']}\nreason: {out['reason']}")
            self.assertNotEquals(out['status'], "ERROR")


    @parameterized.expand([entry_path for entry_path in glob.glob(os.path.join("queries","*.ipynb"))])
    #@unittest.skip("demonstrating skipping")
    def test_all_nb(self, entry_path):
        #for nb in entry_path:
            print(f'Testing {entry_path}')

            with open(entry_path) as f:
                nb = nbformat.read(f, as_version=4)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
                ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}})

                edam_test_output = nb['cells'][-1]['outputs'][0]['text']
                out = json.loads(edam_test_output)
                print()
                print(f"test name: {out['test_name']}")
                print(f"status: {out['status']}")
                print(f"messages:")
                for line in out['reason']:
                    print(f"- {line}")
                self.assertNotEquals(out['status'], "ERROR")


    @unittest.skip("demonstrating skipping")
    def test_exception_nb(self):
        try:
            with open('ci_test/RaisingExceptions.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
                #ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=False)
                ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}})
        except Exception as e:
            print('////////////////////')
            print(type(e))
            print(e)
            print('////////////////////')

        except EdamError as e:
            #print(e)
            #message = str(e.args)
            print('======================')
            print(type(e))
            print(e)
            print('======================')
            #print(message)
        except EdamWarning as e:
            print('======================')
            print(type(e))
            print(e)
            print('======================')
            #print(type(e))

    @unittest.skip("demonstrating skipping")
    def test_fail_nb(self):
        try:
            with open('ci_test/failing_nb.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
                ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}})
        except Exception as e:
            message = str(e.args)
            print(message)
            if "sys.exit(ERROR)" in message :
                print('OK')
                pass
            else:
                print('KO')
                self.fail("Error expected")

    @unittest.skip("demonstrating skipping")
    def test_warn_nb(self):
        try:
            with open('ci_test/warning_nb.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
                ep.preprocess(nb, {'metadata': {'path': 'ci_test/'}})
        except Exception as e:
            message = str(e.args)
            print(message)
            if "sys.exit(WARN)" in message :
                print('OK')
                pass
            else:
                print('KO')
                self.fail("Warning expected")

    def tearDown(self) -> None:
        logging.info("End of unit test")


if __name__ == '__main__':
    unittest.main()
