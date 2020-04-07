# Invalid non-booeal annotation property value

**Problem:** An invalid value was specified for an annotation property that requires a boolean value.

**Solution:** Replace the value with a valid one (currently must always be ```true```).

**Further information:**

There are currently three annotation properties (```owl:deprecated```, ```is_deprecation_candidate```, ```notRecommendedForAnnotation```) that require boolean values; see [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) and [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Query:** [badNonBooleanValue.ipynbl](https://github.com/edamontology/edamverify/blob/master/queries/badNonBooleanValue.ipynb)

