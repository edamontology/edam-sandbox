# EDAM Format concept file extension contains disallowed characters

**Problem:** A file extension specified for an EDAM Format concept contains disallowed characters (they must contain only lowercase alphanumeric characters).

**Solution:** Change the file extension value so that it contains lowercase alphanumeric characters only.

**Further information:** File extensions must not container the period (```.```) or any other disallowed characters. See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Script:** [fileExtensionBadCharacter.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionBadCharacter.ipynb)

