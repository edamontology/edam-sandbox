# EDAM Format concept is missing a mandatory or recommended annotation property

**Problem:** An EDAM Format concept is missing an annotation property that is mandatory or recommended.

**Solution:** Add the missing annotation property.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) for a list of annotation properties that must or should be defined on EDAM Format concepts.  This check does not include properties that are mandatory for *all* concepts. This does not include checks for mandatory relationships - see [formatRelationMissing.md](formatRelationMissing.md).


**Query:** [formatPropertyMissing.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/formatPropertyMissing.ipynb)
