# Deprecated concept with disallowed annotations or axioms

**Problem:** A deprecated concept includes class annotations or axioms which are not allowed.

**Solution:** Remove any disallowed annotation properties or axioms from the deprecated concept.

**Further information:**

Deprecated concepts can only contain certain annotation properties and axioms, as defined [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts).


**Query:** [disallowedDeprecatedContent.sparql](https://github.com/edamontology/edamverify/blob/master/queries/disallowedDeprecatedContent.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
