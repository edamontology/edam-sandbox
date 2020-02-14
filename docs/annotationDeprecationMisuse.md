# Misuse of properties intended for deprecated concepts only

**Problem:** A non-deprecated concept includes annotation properties that are intended solely for use on deprecated concepts.

**Solution:** Remove the misused annotation properties

**Further information** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#deprecating-concepts) for list of applicable annotation properties.


[annotationDeprecationMisuse.sparql]():

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... 
```
