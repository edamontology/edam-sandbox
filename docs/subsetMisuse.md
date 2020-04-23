# Misuse of subset annotation property

**Problem:** The specified EDAM subset for a concept is wrong because: 1) the subset mismatches the subontology (non-deprecated concepts), 2) subset is misstated for deprecated concepts, 3) subsets have multiple (incorrect) subset assignations, 4) Identifier concepts do not have both of 'data' and 'identifiers' subset assignations or 5) subset value is otherwise not supported.

**Solution:** Change the subset to the correct value, as appropriate for the concept subontology and it's deprecation status.

**Further information:**

Concept subset is defined by ```oboInOwl:inSubset``` annotation property and must have an applicable value from ```oboInOwl:SubsetProperty```.

The EDAM [subontology subset](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes) to which the concept has been assigned by setting the ```oboInOwl:inSubset``` to one of ```topic```, ```operation```, ```data``` or ```format``` *must* match the URI [namespace](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#identifiers-persistent-urls) of an EDAM concept ID, *e.g.* ```http://edamontology.org/topic_```.

Deprecated concepts must be assigned to (and only to) the ``obsolete`` subset.

See [EDAM technical details](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes) and [deprecation rules](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts).

**Script:** [subsetMisuse.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/subsetMisuse.ipynb)
