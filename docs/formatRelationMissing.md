#  Concrete format concept is missing mandatory relationships

**Problem:**
A concrete EDAM Format 1) does not descend (via ```subClassOf``` relations) from [Format (by type of data)](http://edamontology.org/format_2350) (or its kids), or 2) does not include an ``is_format_of`` relation to some Data concept.  These relationships are mandatory!

**Solution:** Inspect EDAM and add the missing relationship(s).

**Further information:** Note the rule only applies to [concrete](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#concept-types) Identifier concepts, *i.e.* ones where the ```notRecommendedForAnnotation``` [attribute](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) has not been set to ```true```.  For more information see the guidelines on [hierarchy](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy) and [mandatory concepts](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes).


**Query:** [formatRelationMissing.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/formatRelationMissing.ipynb)

