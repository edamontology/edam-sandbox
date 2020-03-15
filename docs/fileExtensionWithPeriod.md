# EDAM Format concept file extension includes a period character

**Problem:** A file extension specified for an EDAM Format concept includes a period (```.```) character (this is not allowed).

**Solution:** Remove the period character from the file extension value.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Query:** [fileExtensionWithPeriod.sparql](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionWithPeriod.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
