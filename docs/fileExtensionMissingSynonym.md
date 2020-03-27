# EDAM Format concept is missing synyonm or label matching the file extension

**Problem:** A file extension specified for an EDAM Format concept is not also set as the concept label or exactSynonym (this is mandatory).

**Solution:** Ensure that either the concept label or an exact synonym matches the file extension, typically by adding an exact synonym.

**Further information:** For EDAM concepts, the value set for ```<file_extension>``` must also be given for the ```rdfs:label``` or an ```exact_synonym```. See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Script:** [fileExtensionMissingSynonym.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionMissingSynonym.ipynb)
