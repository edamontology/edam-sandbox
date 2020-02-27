# Omission of properties required for deprecated concepts

**Problem:** A deprecated concept lacks required annotation properties.

**Solution:** Add the missing annotation properties.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) for list of applicable annotation properties.


**Query:** [annotationDeprecationOmission.sparql](https://github.com/edamontology/edamverify/blob/master/queries/annotationDeprecationOmission.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
