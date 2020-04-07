#  Wikipedia link missing from EDAM Topic concept

**Problem:** An EDAM Topic concept is missing a link to Wikipedia.

**Solution:** Add a link to an appropriate Wikipedia page for the topic, if available.

**Further information:** The ```documentation``` annotation property is used for Wikipedia URLs (see [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes)).  See also the [Editors Guide](https://edamontologydocs.readthedocs.io/en/latest/editors_guide.html#id5).


**Query:** [wikipediaLinkMissing.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/wikipediaLinkMissing.ipynb)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
