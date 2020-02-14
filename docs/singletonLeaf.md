# Singleton leaf concept

**Problem:** A leaf concept is a singleton, *i.e.* it has no siblings. 

**Solution:** Add relevant sibling concepts to the singleton. Alternatively, if no such concepts exist or can be anticipated, then refactor EDAM to remove the singleton, *e.g.* repositioning it, or deprecating it / consolidating it wiht a parent concept.

**Further information:** None.


**Query:** [singletonLeaf.sparql](https://github.com/edamontology/edamverify/blob/master/queries/singletonLeaf.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
