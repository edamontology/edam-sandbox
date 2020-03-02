# Redundant subclass relationship 

**Problem:** A concept shares a common parent with one of it's ancestors. 

**Solution:** Remove the ```SubClassOf``` relationship (which defines the parent) from the concept.

**Further information:**

A concept must not have a parent if one of it's ancestors already has this parent. See [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy) for examples in the EDAM Identifier and Format subontologies of redundancies that this check captures.


**Query:** [redundantSubclassRelation.sparql](https://github.com/edamontology/edamverify/blob/master/queries/redundantSubclassRelation.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
