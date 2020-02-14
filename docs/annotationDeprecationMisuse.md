# Annotation properties intended for use on deprecatd concepts are used on non-deprecated concepts.
annotationDeprecation


**Problem:** A non-deprecated concept includes annotation properties that are intended solely for use on deprecated concepts.

**Solution:** Remove the misused annotation properties

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... 
```
