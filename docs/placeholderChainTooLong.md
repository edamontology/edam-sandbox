# Chain of placeholder concepts is too long

**Problem:** More than the allowed number of 'placeholder' concepts for a subontology have been chained together.

**Solution:** Refactor EDAM to reduce the length of the chain of 'placeholder' concepts so that it does not exceed the allowed maximum, typically by deprecating one or more placeholders, or other refactoring. 

**Further information:** Concepts are chained together via specialisation (```rdfs:SubClassOf```) relations.  See the [definition](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#placeholder-concepts) of what a 'placholder' concept is, and rules ([here](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#hierarchy-depth) and [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy)) re chaining placholder concepts together.

**Query:** [placeholderChainTooLong.sparql](https://github.com/edamontology/edamverify/blob/master/queries/placeholderChainTooLong.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
