# Concept has multiple parents

**Problem:** A concept has more than one parent where normally just one is expected.

**Solution:** Check EDAM to see if the multiple parentage really is justified, and if it is not,  refactor accordingly.  This typically involves checking the conceptual distinctiveness of the concept and it's parents, followed by merging or deleting concepts, tweaking concept definitions etc.

**Further information:** Concepts normally have only a single parent (implied by ```rdfs:SubClassOf``` relations), but there can be [exceptions](https://edamontologydocs.readthedocs.io/en/latest/editors_guide.html#hierarchy).

**Query:** [unexpectedMultipleParents.sparql](https://github.com/edamontology/edamverify/blob/master/queries/unexpectedMultipleParents.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
