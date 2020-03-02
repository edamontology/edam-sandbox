# Leaf node (concept) is placeholder

**Problem:** An EDAM concept that is a leaf node (no children) has been annotated as being a "placeholder" concept - this is not allowed.

**Solution:** Inspect the offending concept and refactor accordingly, typically either 1) by adding concrete concepts as children of the placeholder, or 2) by redefining the concept to make it more concrete (then remove the placeholder annotation).

**Further information:** 

[Placeholder](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#concept-types) concepts are used primarily to structure EDAM rather than for annotation.  Leaf nodes (concepts without children) should never be placeholders. A placeholder is defined by setting the ```notRecommendedForAnnotation``` annotation property to ```true```. See [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) and [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy) for more information.

**Query:** [placeholderLeafConcept.sparql](https://github.com/edamontology/edamverify/blob/master/queries/placeholderLeafConcept.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
