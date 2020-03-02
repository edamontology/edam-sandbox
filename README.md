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

The problem detected by the query and its remedy are documented in the [docs]() folder.



# Queries
Query                    | Level | Docs | Issue| File | Status
-----                    | ----- | ---- | ---- | ---- | ------
Dummy test SPARQL query  | INFO | - | [1](https://github.com/edamontology/edamverify/issues/1) | [test_sparql.sparql](queries/test_sparql.sparql) | todo
Dummy test SHACL query   | INFO | - | [2](https://github.com/edamontology/edamverify/issues/2) | [test_shacl.shacl](queries/test_shacl.shacl) | todo
Omission of properties required for deprecated concepts | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/annotationDeprecationOmission.md) | [3](https://github.com/edamontology/edamverify/issues/3) | [annotationDeprecationOmission.sparql](queries/annotationDeprecationOmission.sparql) | todo
Misuse of properties intended for deprecated concepts only | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/annotationDeprecationMisuse.md) | [2](https://github.com/edamontology/edamxpathvalidator/issues/2) | [annotationDeprecationMisuse.sparql](queries/annotationDeprecationMisuse.sparql) | todo
Ontology max depth exceeded | WARN | [docs](https://github.com/edamontology/edamverify/blob/master/docs/maxDepthExceeded.md) | [6](https://github.com/edamontology/edamxpathvalidator/issues/6) | [maxDepthExceeded.sparql](queries/maxDepthExceeded.sparql) | todo
Singleton leaf node | WARN | [docs](https://github.com/edamontology/edamverify/blob/master/docs/singletonLeaf.md) | [7](https://github.com/edamontology/edamxpathvalidator/issues/7) | [singletonLeaf.sparql](queries/singletonLeaf.sparql) | todo
Subset misuse | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/subsetMisuse.md) | [14](https://github.com/edamontology/edamxpathvalidator/issues/14) | [subsetMisuse.sparql](queries/subsetMisuse.sparql) | todo
Disallowed synonym | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/disallowedSynonym.md) | [11](https://github.com/edamontology/edamxpathvalidator/issues/11) | [disallowedSynonym.sparql](queries/disallowedSynonym.sparql) | todo
Placeholder chain too long | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/placeholderChainTooLong.md) | [8](https://github.com/edamontology/edamxpathvalidator/issues/8) | [placeholderChainTooLong.sparql](queries/placeholderChainTooLong.sparql) | todo
Unexpected multiple parents | WARN | [docs](https://github.com/edamontology/edamverify/blob/master/docs/unexpectedMultipleParents.md) | [9](https://github.com/edamontology/edamxpathvalidator/issues/9) | [unexpectedMultipleParents.sparql](queries/unexpectedMultipleParents.sparql) | todo
Possible spelling mistake | INFO | [docs](https://github.com/edamontology/edamverify/blob/master/docs/spellingMistake.md) | [10](https://github.com/edamontology/edamxpathvalidator/issues/10) | [spellingMistake.sparql](queries/spellingMistake.sparql) | todo
Bad EDAM URI reference | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/badEdamUriReference.md) | [12](https://github.com/edamontology/edamxpathvalidator/issues/12) | [badEdamUriReference.sparql](queries/badEdamUriReference.sparql) | todo
Bad non-boolean value | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/badNonBooleanValue.md) | [13](https://github.com/edamontology/edamxpathvalidator/issues/13) | [badNonBooleanValue.sparql](queries/badNonBooleanValue.sparql) | todo
Mandatory property missing | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/mandatoryPropertyMissing.md) | [8](https://github.com/edamontology/edamverify/issues/8) | [mandatoryPropertyMissing.sparql](queries/mandatoryPropertyMissing.sparql) | todo
Format property missing | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/formatPropertyMissing.md) | [9](https://github.com/edamontology/edamverify/issues/8) | [formatPropertyMissing.sparql](queries/formatPropertyMissing.sparql) | todo
Identifier property missing | ERROR | [docs](https://github.com/edamontology/edamverify/blob/master/docs/identifierPropertyMissing.md) | [10](https://github.com/edamontology/edamverify/issues/8) | [identifierPropertyMissing.sparql](queries/identifierPropertyMissing.sparql) | todo
Wikipedia link missing | INFO | [docs](https://github.com/edamontology/edamverify/blob/master/docs/wikipediaLinkMissing.md) | [10](https://github.com/edamontology/edamverify/issues/8) | [wikipediaLinkMissing.sparql](queries/wikipediaLinkMissing.sparql) | todo

# General queries (from [ROBOT report](http://robot.obolibrary.org/report))
Query                         | Description | Level
----------------------------- | ----------- | -----
annotation whitespace	      | [link](http://robot.obolibrary.org/report_queries/annotation_whitespace)    | WARN
deprecated boolean datatype   | [link](http://robot.obolibrary.org/report_queries/deprecated_boolean_datatype)    | ERROR
deprecated class reference    | [link](http://robot.obolibrary.org/report_queries/deprecated_class_reference)    | ERROR
deprecated property reference |	[link](http://robot.obolibrary.org/report_queries/deprecated_property_reference)    | ERROR
duplicate definition	      | [link](http://robot.obolibrary.org/report_queries/duplicate_definition)    | ERROR
duplicate exact synonym	      | [link](http://robot.obolibrary.org/report_queries/duplicate_exact_synonym)    | WARN
duplicate label synonym	      | [link](http://robot.obolibrary.org/report_queries/duplicate_label_synonym)    | WARN
duplicate label	              | [link](http://robot.obolibrary.org/report_queries/duplicate_label)    | ERROR
duplicate scoped synonym      | [link](http://robot.obolibrary.org/report_queries/duplicate_scoped_synonym)    | WARN
equivalent pair	              | [link](http://robot.obolibrary.org/report_queries/equivalent_pair)    | WARN
invalid xref	              | [link](http://robot.obolibrary.org/report_queries/invalid_xref)    | WARN
label formatting	      | [link](http://robot.obolibrary.org/report_queries/label_formatting)    | ERROR
label whitespace	      | [link](http://robot.obolibrary.org/report_queries/label_whitespace)    | ERROR
lowercase definition	      | [link](http://robot.obolibrary.org/report_queries/lowercase_definition)    | INFO
missing definition	      | [link](http://robot.obolibrary.org/report_queries/missing_definition)    | WARN
missing label	              | [link](http://robot.obolibrary.org/report_queries/missing_label)    | ERROR
missing obsolete label	      | [link](http://robot.obolibrary.org/report_queries/missing_obsolete_label)    | WARN
missing ontology description  | [link](http://robot.obolibrary.org/report_queries/missing_ontology_description)    | ERROR
missing ontology license      | [link](http://robot.obolibrary.org/report_queries/missing_ontology_license)    | ERROR
missing ontology title	      | [link](http://robot.obolibrary.org/report_queries/missing_ontology_title)    | ERROR
missing superclass	      | [link](http://robot.obolibrary.org/report_queries/missing_superclass)    | INFO
misused obsolete label	      | [link](http://robot.obolibrary.org/report_queries/misused_obsolete_label)    | ERROR
multiple definitions	      | [link](http://robot.obolibrary.org/report_queries/multiple_definitions)    | ERROR
multiple equivalent classes   | [link](http://robot.obolibrary.org/report_queries/multiple_equivalent_classes)    | ERROR
multiple labels	              | [link](http://robot.obolibrary.org/report_queries/multiple_labels)    | ERROR


# Files

File                            | Description
----                            | -----------
src/edamverify.py               | edamverify utility
queries/                        | Queries in SPARQL query language and SHACL constraint language format
docs/                           | Query documentation (the problem detected by the query and its remedy)
reports/                        | Reports from running edamverify on EDAM_dev.owl
README.md		        | This file






