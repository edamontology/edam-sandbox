**UNDER CONSTRUCTION - edamverify is being built and the docs here describe the intended state, not it's current state!**

# EDAM Verification Utility : edamverify

**edamverify** is a utility for verification of the EDAM ontology.  It implements a set of quality control (QC) checks based upon:

* Guidelines from the [Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html) for
  - [adding concepts](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#adding-concepts)
  - [hierarchy structure](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy)
  - [deprecating concepts](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts)
* [Rules of thumb for EDAM development](https://edamontologydocs.readthedocs.io/en/latest/editors_guide.html#rules-of-thumb-for-edam-development) from the [Editors Guide](https://edamontologydocs.readthedocs.io/en/latest/editors_guide.html)
   
edamverify implements all checks previously implemented in [edamxpathvalidator](https://github.com/edamontology/edamxpathvalidator).

edamverify is invoked whenever the development copy of EDAM ([EDAM_dev.owl](https://github.com/edamontology/edamontology/blob/master/EDAM_dev.owl)) is changed, using the EDAM Travis CI system.


# EDAM QC implementation
EDAM QC consists of:
* invocation of the [report](http://robot.obolibrary.org/report) utility from the [ROBOT](https://github.com/ontodev/robot) ontology verification suite.  This runs a [series](http://robot.obolibrary.org/report_queries/) of basic quality control SPARQL queries, such as duplicated labels or synyonms, missing ontology metadata, references to deprecated concepts *etc.*
* invocation of **edamverify** which runs a series of SPARQL and SHACL queries, defined in the `queries/` folder (see below) which are tailored specifically to EDAM.  The SPARQL queries are invoked using the ROBOT [verify](http://robot.obolibrary.org/verify) utility.  The SHACL queries are invoked directly.

Each query has a logging level (based on [ROBOT report](http://robot.obolibrary.org/report)) which defines the severity of the issue: 
* **ERROR**: Must be fixed before releasing EDAM. These issues will cause problems for users, such as classes with multiple labels.
* **WARN**: Should be fixed as soon as possible. These will not cause problems for all users, but may not be what they expect. For example, a class that is inferred to be equivalent to another named class.
* **INFO**: Should be fixed if possible. These are for consistency and cleanliness, such as definitions that do not start with an uppercase character.


# Queries
Query              | Description              | Level | File                                             | Issue
-----              | ------------------------ | ----- | ------------------------------------------------ | -----
test_sparql        | Dummy test SPARQL query  | INFO  | [test_sparql.sparql](queries/test_sparql.sparql) | [1](https://github.com/edamontology/edamverify/issues/1)
test_shacl         | Dummy test SHACL query   | INFO  | [test_shacl.shacl](queries/test_shacl.shacl)     | [2](https://github.com/edamontology/edamverify/issues/2)


# Files

File                            | Description
----                            | -----------
src/edamverify.py               | edamverify utility
queries/                        | Queries in SPARQL query language and SHACL constraint language format
reports/                        | Reports from running edamverify on EDAM_dev.owl
README.md		        | This file






