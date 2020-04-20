# Misuse of subset annotation property

**Problem:** The specified EDAM subset for a concept is wrong because the value: 1) mismatches the subontology (non-deprecated concepts), 2) is misstated (deprecated concepts), or 3) is otherwise not supported.

**Solution:** Change the subset to the correct value, as appropriate for the concept subontology and it's deprecation status.

**Further information:**

Concept subset is defined by ```oboInOwl:inSubset``` annotation property and must have an applicable value from ```oboInOwl:SubsetProperty```. The EDAM [subontology subset](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes) to which the concept has been assigned by setting the ```oboInOwl:inSubset``` to one of ```topic```, ```operation```, ```data``` or ```format``` *must* match the URI [namespace](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#identifiers-persistent-urls) of an EDAM concept ID, *e.g.* ```http://edamontology.org/topic_```.

See [EDAM technical details](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes) and [deprecation rules](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts).

**Script:** [subsetMisuse.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/subsetMisuse.ipynb)
