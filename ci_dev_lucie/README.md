Complementory to the queries implemented using robot report tool, here are specific EDAM queries to test the owl file \
\
check_wikipedia_link.rq 		| sparql query, checks that every topic has a wikipedia link filled in the seeAlso property \
concept_id_inferior_to_next_id.rq	| sparql query, checks that the numerical id associated with a concept if inferior to the next id property (header of OWL file)\
deprecated_replacement_obsolete.rq	| sparql query, checks that the suggested replacement (replacedBy/consider) for deprecated term is not obsolete\
deprecated_replacement.rq		| sparql query, checks that every deprecated concept has a replacement suggested (replacesby or consider) \
end_dot_def_missing.rq			| sparql query, checks if a dot is missing at the end of the definition property \
end_dot_label.rq 			| sparql query, ensure there is not dot at the end of the label property  \
end_space_annotation.rq			| sparql query, checks that there is no space at the end of the annotations\
eol_in_annotation.rq 			| sparql query, checks that there is no end of line in the annotations  \
formating.rq				| sparql query, summurize the query  end_space_annotation.rq, eol_in_annotation.rq, start_space_annotation.rq, tab_in_annotation.rq \
format_property_missing.rq		| sparql query, checks the no "mandatory" property for format are missing\
identifier_property_missing.rq		| sparql query, checks the no "mandatory" property for all concept are missing\
id_unique.rq				| sparql query, (testing not finished) check that no numeriacal part of is duplicated\
mandatory_property_missing.rq		| sparql query, checks the no mandatory property for identifier are missing\
missing_deprecated_property.rq		| sparql query, checks that no mandatory property for deprecated concept are missing\
missing_format-data_relation.rq		| sparql query, checks that there is a relation format-data for each data \
object_relation_obsolete.rq		| sparql query, checks that the relation between concept are not pointing towards obsolete concepts\
operation_input_output_too_broad.rq	| sparql query, checks that the input and output of operation is different from the root concept Data, which is too broad\
prefix_query				| prefix for sparql query - name space in EDAM\
queries.conf\
start_space_annotation.rq 		| sparql query, checks if there is a space at the start of the annotations \
super_class_refers_to_self.rq		| sparql query, checks if a given consept doesn't refers to itself as superclass \
tab_in_annotation.rq			| sparql query, checks if there is a tabulation in the annotations \
template_query.rq			\
test.conf\
test query-Copy1.ipynb'			| test for implemting above queries \
test query.ipynb'\
\
For each query, there is an associated 'Run <query> .ipynb' file \
\
\
