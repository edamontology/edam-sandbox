import filecmp
import os
import tempfile
import unittest
from xml.dom import minidom
import xml.etree.ElementTree as ET

from rdflib import Graph, URIRef, RDF, OWL, Namespace

from edamfu.core import load, save, CANONICAL_NAMESPACES


def get_temporary_file_path():
    # Create a temporary file and return its path
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name
    temp_file.close()
    return temp_file_path


def get_ontology_subject(graph):
    # Test for the presence of owl:Ontology
    ontology_subjects = [
        subject
        for subject in graph.subjects(RDF.type, OWL.Ontology)
        if all(
            triple_object != OWL.Class
            for _, _, triple_object in graph.triples((subject, RDF.type, None))
        )
    ]
    return ontology_subjects[0] if ontology_subjects else None


def retrieve_element_from_xml(xml_file_path, element_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    return root.findall(element_path)


def compare_xml_elements(elem1, elem2, tag=''):
    if elem1.tag != elem2.tag:
        return False, f"tag `{tag}`: Tags {elem1.tag} and {elem2.tag} are different"
    if elem1.text and elem2.text and elem1.text != elem2.text:
        text1 = elem1.text.replace(' ', '\u2423').replace(' ', '\u2192').replace('\n', '\u240A')
        text2 = elem2.text.replace(' ', '\u2423').replace(' ', '\u2192').replace('\n', '\u240A')
        return False, f"tag `{tag}`: Text `{text1}` and `{text2}` are different"
    elif (elem1.text and not elem2.text) or (not elem1.text and elem2.text):
        return False, f"tag `{tag}`: Text {elem1.text} and {elem2.text} are different"        
    if elem1.attrib != elem2.attrib:
        return False, f"tag `{tag}`: Attributes {elem1.attrib} and {elem2.attrib} are different"
    if len(elem1) != len(elem2):
        return False, f"tag `{tag}`: Number of children {len(elem1)} and {len(elem2)} are different"
    for child1, child2 in zip(elem1, elem2):
        res, msg = compare_xml_elements(child1, child2, tag=tag+'/'+elem1.tag)
        if not res:
            return res, msg
    return True, "all elements are identical"

def get_pretty_xml(element):
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

class CoreTestCase(unittest.TestCase):
    # Test loading the "raw" EDAM ontology from a file, and then saving it to another file

    @classmethod
    def setUpClass(cls):
        # Set up any necessary test data or resources
        cls.edam_file_raw_path = "EDAM_dev.owl"
        g = load(cls.edam_file_raw_path)
        cls.result_file_path = get_temporary_file_path()
        save(g, cls.result_file_path)
        cls.result_graph = Graph()
        cls.result_graph.parse(cls.result_file_path, format="xml")

    @classmethod
    def tearDownClass(cls):
        #print(retrieve_element_from_xml(cls.edam_file_raw_path, ".//{http://www.w3.org/2002/07/owl#}Ontology"))
        #print(retrieve_element_from_xml(cls.result_file_path, ".//{http://www.w3.org/2002/07/owl#}Ontology"))
        #if cls.result_file_path and os.path.exists(cls.result_file_path):
        #    os.remove(cls.result_file_path)
        return  

    def test_ontology_class_exists(self):
        # there should be an ontology class in the result graph
        self.assertIsNotNone(
            get_ontology_subject(self.result_graph),
            f"Cannot find the ontology class in the result graph of file {self.result_file_path}",
        )

    def test_ontology_elements_identical(self):
        # the result should be the same as the original file
        raw_onto_el = retrieve_element_from_xml(self.edam_file_raw_path, ".//{http://www.w3.org/2002/07/owl#}Ontology")[0]
        result_onto_el = retrieve_element_from_xml(self.result_file_path, ".//{http://www.w3.org/2002/07/owl#}Ontology")[0]
        res, msg = compare_xml_elements(raw_onto_el, result_onto_el)
        self.assertTrue(
            res,
            f"Ontology elements in {self.edam_file_raw_path} and {self.result_file_path} are not identical because {msg}",
            #f"Ontology elements in {self.edam_file_raw_path} and {self.result_file_path} are not identical because {msg}:\n\n {get_pretty_xml(raw_onto_el)}\n\n vs \n\n{get_pretty_xml(result_onto_el)}",
        )   

    def test_files_identical(self):
        # the result should be the same as the original file
        self.assertTrue(
            filecmp.cmp(self.edam_file_raw_path, self.result_file_path),
            f"Files {self.edam_file_raw_path} and {self.result_file_path} are not identical",
        )


if __name__ == "__main__":
    unittest.main()
