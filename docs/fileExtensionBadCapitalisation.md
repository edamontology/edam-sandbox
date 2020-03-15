# EDAM Format concept file extension is not lower-case

**Problem:** A file extension specified for an EDAM Format concept is not in lowercase (it must be).

**Solution:** Change the file extension value so that it is in lowercase.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Query:** [fileExtensionBadCapitalisation.sparql](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionBadCapitalisation.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
