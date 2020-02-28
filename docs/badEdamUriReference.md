# A URI in the EDAM concept namespace is references but does not exist

**Problem:** A URI in the EDAM concept namespace is referenced from somwhere in EDAM, but there is no corresponding concept definition for this URI.

**Solution:** Explore and correct the reference, which most likely will be a typo and should be changed to a URI for which a concept definition exists.

**Further information:**

There are four EDAM concept namespaces (one per subontology) *e.g.* ```http://edamontology.org/topic_```.  See [here](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html?highlight=namespac#identifiers-persistent-urls) for more information.


**Query:** [badEdamUriReference.sparql](https://github.com/edamontology/edamverify/blob/master/queries/badEdamUriReference.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
