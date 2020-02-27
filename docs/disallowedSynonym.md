# narrowSynonym or broadSynonym defined in Format subontology

**Problem:** A ```narrowSynonym``` or ```broadSynonym``` was defined on a concept in the Format subontology - this is not allowed.

**Solution:** Either remove the ```narrowSynonym``` or ```narrowSynonym```, or replace it with an ```exactSynonym```. 

**Further information:** See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) re for information requirement for attributes on subontologies.

**Query:** [disallowedSynonym.sparql](https://github.com/edamontology/edamverify/blob/master/queries/disallowedSynonym.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
