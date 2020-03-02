# EDAM Format concept is missing a mandatory annotation propery

**Problem:** An EDAM Format concept is missing an annotation property that is mandatory.

**Solution:** Add the missing annotation property.

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) for a list of annotation properties that must be defined on EDAM Format concepts.  This check does not include properties that are mandatory for *all* concepts.


**Query:** [formatPropertyMissing.sparql](https://github.com/edamontology/edamverify/blob/master/queries/formatPropertyMissing.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
