# EDAM concept is missing a mandatory annotation propery

**Problem:** A concept is missing an annotation property that is mandatory for all EDAM concepts.

**Solution:** Add the missing annotation property.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) for a list of annotation properties that must be defined on all EDAM concepts.


**Query:** [mandatoryPropertyMissing.sparql](https://github.com/edamontology/edamverify/blob/master/queries/mandatoryPropertyMissing.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
