# EDAM Format concept is missing synyonm for file extension

**Problem:** A file extension specified for an EDAM Format concept does not also appear as an ```exactSynonym``` of that concept (this is mandatory).

**Solution:** Add the missing synonym(s). For example for the file extension ```txt``` two synyonms should be specified: ```.txt``` and ```txt```.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Query:** [fileExtensionMissingSynonym.sparql](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionMissingSynonym.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
