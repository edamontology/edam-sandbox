# edamverifylib - library of common functions for EDAM verification
# Library for processing the following JSON object:
# {
#   'test_name' : "Name of test",
#   'comment' : "Note about the test."
#   'status' : "ERROR_CODE"
#   'reason':
#   [
#       "Report line 1",
#       "Report line 2",
#       "Report line n"
#   ]
# }
#
# Permissible values of ERROR_CODE are defined above (NOERR, INFO etc.)
#
# TODO - REWRITE TO USE PYTHON F STRINGS ONCE I UPDATE MY PYTHON ENVIRONMENT

import json


# Global variables
NOERR = "NOERR"
INFO  = "INFO"
WARN  = "WARN"
ERROR = "ERROR"


class EdamReport:
    """edamverify report class - stores the results from running a QA test"""


    def __init__(self, testname, comment, status, reason):
        """Initialise an EdamReport object"""
        self.testname = testname
        self.comment = comment
        self.status = status
        self.reason = reason

    def reportWriteMd(self):
        """Print an error report in GitHub md format"""
        print("#", self.testname)
        print("**STATUS**: ", self.status, "\n")
        print(self.comment)
        for a_reason in self.reason:
            print("* ", a_reason)

    def reportWriteJson(self):
        """Print an error report in JSON format"""
        print(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))

        # Explanation of above code.
        #         # "default=" specifies the serialisation function - it's required for objects such as EdamReport that can't otherwise be serialisised.
        #         # "lambda o:" defines an anonymous function (or lambda function) with a single parameter - "o"
        #         # o.__dict__ is the argument to the lambda function - a dictionary of the object's (writable) attributes
        #         #
        #         # It's a short-hand equivalent to:
        #         # report_obj = {}
        #         # report_obj['test_name'] = self.testname
        #         # report_obj['comment'] = self.comment
        #         # report_obj['status'] = self.status
        #         # report_obj['reason'] = self.reason
        #         # report_json = json.dumps(report_obj, indent=4)
        # print(report_json)