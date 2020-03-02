#  File extension missing from EDAM Format concept

**Problem:** An EDAM Format concept is missing a file extension.

**Solution:** Add the file extension.

**Further information:** The ```file_extension``` annotation property is used to specify the common file extension(s) of a data format. See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) and [Editors Guide](https://edamontologydocs.readthedocs.io/en/latest/editors_guide.html#id12) for more information.


**Query:** [formatFileExtensionMissing.sparql](https://github.com/edamontology/edamverify/blob/master/queries/formatFileExtensionMissing.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
