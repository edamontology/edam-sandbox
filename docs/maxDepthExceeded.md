# Maximum depth of ontology exceeded

**Problem:** The depth of EDAM exceeds the recommended maximum depth (a chain of `subClass` relations is too long).

**Solution:** Refactor EDAM to decrease the depth by refactoring the conceptual hierarchy, typically by nesting the offending concept elsewhere, deprecating superfluous placholder concepts, consolidating overly-specialised concepts, or other changes. 

**Further information:** See [EDAM Technical details](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#hierarchy-depth) for hierarchy depth rules and the [Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy) for further information.


**Query:** [maxDepthExceeded.sparql](https://github.com/edamontology/edamverify/blob/master/queries/maxDepthExceeded.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
