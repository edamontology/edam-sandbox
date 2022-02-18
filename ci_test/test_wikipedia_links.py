import unittest
import logging, sys
from parameterized import parameterized
import glob
import os
import json

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    stream=sys.stdout,
)


class TestNotebooks(unittest.TestCase):
    def setUp(self) -> None:
        logging.info("Logger intialized ! ")

    @parameterized.expand(
        [
            entry_path
            for entry_path in glob.glob(os.path.join(".", "wikipedia_links.ipynb"))
        ],
        skip_on_empty=True,
    )
    def test_all_nb(self, entry_path):
        # for nb in entry_path:
        print(f"Testing {entry_path}")

        with open(entry_path) as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
            ep.preprocess(nb, {"metadata": {"path": "."}})

            for cells in reversed(nb["cells"]):
                if cells["outputs"]:
                    edam_test_output = cells["outputs"][0]["text"]
                    break
            print(edam_test_output)
            # out = json.loads(edam_test_output)
            # print(f"test name: {out['test_name']}\nstatus: {out['status']}\nreason: {out['reason']}")
            self.assertFalse("error" in edam_test_output.lower())

    def tearDown(self) -> None:
        logging.info("End of unit test")


if __name__ == "__main__":
    unittest.main()
