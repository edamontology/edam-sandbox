
import unittest


class DiffTestCase(unittest.TestCase):
    
    ref = """
@prefix ns1: <http://www.geneontology.org/formats/oboInOwl#> .
@prefix ns2: <http://edamontology.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ns2:data_0852 a owl:Class ;
    rdfs:label "Sequence mask type" ;
    ns2:created_in "beta12orEarlier" ;
    ns2:obsolete_since "1.5" ;
    ns1:consider ns2:data_0842 ;
    ns1:hasDefinition "A label (text token) describing the type of sequence masking to perform." ;
    ns1:inSubset <http://purl.obolibrary.org/obo/edam#obsolete> ;
    rdfs:comment "Sequence masking is where specific characters or positions in a molecular sequence are masked (replaced) with an another (mask character). The mask type indicates what is masked, for example regions that are not of interest or which are information-poor including acidic protein regions, basic protein regions, proline-rich regions, low compositional complexity regions, short-periodicity internal repeats, simple repeats and low complexity regions. Masked sequences are used in database search to eliminate statistically significant but biologically uninteresting hits." ;
    rdfs:subClassOf owl:DeprecatedClass ;
    owl:deprecated "true" .

ns2:data_0853 a owl:Class ;
    rdfs:label "DNA sense specification" ;
    ns2:created_in "beta12orEarlier" ;
    ns2:obsolete_since "1.20" ;
    ns2:oldParent ns2:data_2534 ;
    ns1:consider ns2:data_2534 ;
    ns1:hasDefinition "The strand of a DNA sequence (forward or reverse)." ;
    ns1:inSubset <http://purl.obolibrary.org/obo/edam#obsolete> ;
    rdfs:comment "The forward or 'top' strand might specify a sequence is to be used as given, the reverse or 'bottom' strand specifying the reverse complement of the sequence is to be used." ;
    rdfs:subClassOf owl:DeprecatedClass ;
    owl:deprecated "true" .
    """
    
    # @classmethod
    # def setUpClass(cls):
    #     # Set up any necessary test data or resources
    #     cls.edam_file_raw_path = "EDAM_dev.owl"
    #     g = load(cls.edam_file_raw_path)
    #     cls.result_file_path = get_temporary_file_path()
    #     save(g, cls.result_file_path)
    #     cls.result_graph = Graph()
    #     cls.result_graph.parse(cls.result_file_path, format="xml")

    # @classmethod
    # def tearDownClass(cls):
    #     #print(retrieve_element_from_xml(cls.edam_file_raw_path, ".//{http://www.w3.org/2002/07/owl#}Ontology"))
    #     #print(retrieve_element_from_xml(cls.result_file_path, ".//{http://www.w3.org/2002/07/owl#}Ontology"))
    #     #if cls.result_file_path and os.path.exists(cls.result_file_path):
    #     #    os.remove(cls.result_file_path)
    #     return  

    def test_reordered_classes(self):
        print("test_reordered_classes")


if __name__ == "__main__":
    unittest.main()