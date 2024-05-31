import csv
from flask import Flask, redirect, url_for, request, render_template
import random
import os

from rdflib import ConjunctiveGraph, Namespace

app = Flask(__name__)

ns = {"dc": "http://dcterms/",
      "edam": "http://edamontology.org/",
      "owl": "http://www.w3.org/2002/07/owl#"
      }

g = ConjunctiveGraph()
g.parse('https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl', format='xml')
g.bind('edam', Namespace('http://edamontology.org/'))
print(str(len(g)) + ' triples in the EDAM triple store')

g_last_stable = ConjunctiveGraph()
g_last_stable.parse('http://edamontology.org/EDAM.owl', format='xml')

## Build an index to retrieve term labels 
idx_label = {}
idx_uri = {}
idx_query = """
SELECT ?x ?label WHERE {
    ?x rdf:type owl:Class ; 
       rdfs:label ?label .
}
"""
results = g.query(idx_query)
for r in results :
    #print(f"{r['label']} is identified in EDAM with concept {r['x']}") 
    idx_uri[str(r['x'])] = str(r['label'])
    idx_label[str(r['label'])] = str(r['x'])

@app.route('/')
def index():
    res = get_edam_numbers(g)
    res_last = get_edam_numbers(g_last_stable)

    return render_template('index.html',
                           topics=res['nb_topics'],
                           operations=res['nb_operations'],
                           data=res['nb_data'],
                           formats=res['nb_formats'],
                           new_topics=res['nb_topics'] - res_last['nb_topics'],
                           new_operations=res['nb_operations'] - res_last['nb_operations'],
                           new_data=res['nb_data'] - res_last['nb_data'],
                           new_formats=res['nb_formats'] - res_last['nb_formats']
                           )

@app.route('/current')
def current():
    res = get_edam_numbers(g)

    return render_template('current.html',
                           topics=res['nb_topics'],
                           operations=res['nb_operations'],
                           data=res['nb_data'],
                           formats=res['nb_formats']
                           )

@app.route('/quality')
def quality():
    res = get_edam_numbers(g)

    return render_template('quality.html',
                           topics=res['nb_topics'],
                           operations=res['nb_operations'],
                           data=res['nb_data'],
                           formats=res['nb_formats']
                           )

def get_edam_numbers(g):
    query_op = """
    SELECT DISTINCT ?x WHERE {
        ?x rdfs:subClassOf+ <http://edamontology.org/operation_0004> .
    }
    """
    results = g.query(query_op)
    nb_op = len(results)

    query_top = """
    SELECT DISTINCT ?x WHERE {
        ?x rdfs:subClassOf+ <http://edamontology.org/topic_0003> .
    }
    """
    results = g.query(query_top)
    nb_top = len(results)

    query_data = """
    SELECT DISTINCT ?x WHERE {
        ?x rdfs:subClassOf+ <http://edamontology.org/data_0006> .
    }
    """
    results = g.query(query_data)
    nb_data = len(results)

    query_formats = """
    SELECT DISTINCT ?x WHERE {
        ?x rdfs:subClassOf+ <http://edamontology.org/format_1915> .
    }
    """
    results = g.query(query_formats)
    nb_formats = len(results)

    return {'nb_topics': nb_top, 
            'nb_operations': nb_op, 
            'nb_data': nb_data, 
            'nb_formats': nb_formats}


@app.route('/edam_stats')
def edam_stats():

    res = get_edam_numbers(g)
    res_last = get_edam_numbers(g_last_stable)

    return render_template('stats.html', 
        topics = res['nb_topics'], 
        operations = res['nb_operations'],
        data = res['nb_data'],
        formats = res['nb_formats'],
        new_topics = res['nb_topics'] - res_last['nb_topics'], 
        new_operations = res['nb_operations'] - res_last['nb_operations'], 
        new_data = res['nb_data'] - res_last['nb_data'], 
        new_formats = res['nb_formats'] - res_last['nb_formats']
        )
    
@app.route('/edam_validation')
def edam_validation():
    return render_template('index.html')

@app.route('/edam_last_report')
def edam_last_report():
    number=0
    # edam ci report
    with open("test_data/output_edamci.tsv") as file:
        output_edamci = csv.DictReader(file, delimiter="\t")
        edamci_output_list = []
        for row in output_edamci:
            row["Number"]=number
            number+=1
            edamci_output_list.append(row)
        # robot report
    with open("test_data/report_profile.tsv") as file:
        robot_output = csv.DictReader(file, delimiter="\t")
        robot_output_list = []
        for row in robot_output:
            row["Label"]=idx_uri[row["Subject"]]
            row["Number"]=number
            number+=1
            robot_output_list.append(row)    

    return render_template('edam_last_report.html', output_edamci_list=edamci_output_list, robot_output_list=robot_output_list)

#################################################
# How to contribute
#################################################
@app.route('/high_priority')
def high_priority():
    dir_queries = "./queries"

    ## Checks that all mandatory properties are filled in.
    query = dir_queries + "/mandatory_property_missing.rq"
    with open(query, "r") as f:
        query = f.read()
        results = g.query(query)
    f.close()

    mandatory_property_missing = []
    for r in results:
        mandatory_property_missing.append({"term": r["label"], "class": r["entity"]})

    ## Checks that all IDs have a unique number.
    query = dir_queries + "/get_uri.rq"
    with open(query, "r") as f:
        query = f.read()
        results = g.query(query)
    f.close()

    id_unique = []
    for r in results:
        id_unique.append({"term": r["label"], "class": r["entity"]})

    return render_template('high_priority.html',
                            mandatory_property_missing = mandatory_property_missing,
                            id_unique = id_unique,
                            random = random)

####################################
@app.route('/quick_curation')
def quick_curation():

    dir_queries = "./queries"

    ## Checks that all webpage and doi are declared as literal links.
    query = dir_queries + "/literal_links.rq"
    with open(query, "r") as f:
        query = f.read()
        results = g.query(query)
    f.close()

    literal_links = []
    for r in results:
        literal_links.append({"term": r["label"], "class": r["entity"]})

    ## Formatting of def and labels 
    # end_dot_def_missing.rq;end_dot_label.rq;end_space_annotation.rq;eol_in_annotation.rq;start_space_annotation.rq;tab_in_annotation.rq
    queries = [ dir_queries + "/end_dot_def_missing.rq", dir_queries + "/end_dot_label.rq", dir_queries + "/end_space_annotation.rq", dir_queries + "/eol_in_annotation.rq", 
               dir_queries + "/start_space_annotation.rq", dir_queries + "/tab_in_annotation.rq"]
    results = {}
    for q in queries:
        with open(q, "r") as f:
            q = f.read()
            results.update(g.query(q))
        f.close()

    formatting = []
    for r in results:
        formatting.append({"term": r["label"], "class": r["entity"]})

    ## Get topics without a wikipedia link (WARNING)
    query = dir_queries + "/no_wikipedia_link_topic.rq"
    with open(query, "r") as f:
        query = f.read()
        results = g.query(query)
    f.close()

    no_wikipedia_link_topic = []
    for r in results:
        no_wikipedia_link_topic.append({"term": r["term"], "class": r["concept"]})

    # ## Get operations without a wikipedia link (WARNING)
    # query = dir_queries + "/no_wikipedia_link_operation.rq"
    # with open(query, "r") as f:
    #     query = f.read()
    #     results = g.query(query)
    # f.close()

    # no_wikipedia_link_operation = []
    # for r in results:
    #     no_wikipedia_link_operation.append({"term": r["term"], "class": r["concept"]})

    # ## Get topics without any broad synonym (OPTIONAL)
    # query = dir_queries + "/no_broad_synonym_topic.rq"
    # with open(query, "r") as f:
    #     query = f.read()
    #     results = g.query(query)
    # f.close()

    # no_broad_synonym_topic = []
    # for r in results:
    #     no_broad_synonym_topic.append({"term": r["term"], "class": r["concept"]})

    # ## Get topics without a definition (ERROR)
    # query = dir_queries + "/no_definition_topic.rq"
    # with open(query, "r") as f:
    #     query = f.read()
    #     results = g.query(query)
    # f.close()

    # no_definition_topic = []
    # for r in results:
    #     no_definition_topic.append({"term": r["term"], "class": r["concept"]})


    # NO wikipedia
    # q_no_wikipedia = """
    # SELECT (count(?term) as ?nb_no_wikipedia) WHERE {
    #     ?c rdfs:subClassOf+ edam:topic_0003 ;
    #                 rdfs:label ?term .
    #
    #     FILTER NOT EXISTS {
    #         ?c rdfs:seeAlso ?seealso .
    #         FILTER (regex(str(?seealso), "wikipedia.org", "i"))
    #     } .
    # }
    # """
    #
    # results = g.query(q_no_wikipedia, initNs=ns)
    # count_no_wikipedia = 0
    # for r in results:
    #     count_no_wikipedia = str(r["nb_no_wikipedia"])

    # #########
    # q_no_wikipedia_all = """
    #     SELECT ?c ?term WHERE {
    #         ?c rdfs:subClassOf+ edam:topic_0003 ;
    #             rdfs:label ?term .
    #
    #         FILTER NOT EXISTS {
    #             ?c rdfs:seeAlso ?seealso .
    #             FILTER (regex(str(?seealso), "wikipedia.org", "i"))
    #         } .
    #     }
    #     """
    # results = g.query(q_no_wikipedia_all, initNs=ns)
    # no_wikipedia = []
    # for r in results:
    #     no_wikipedia.append({"term": r["term"], "class": r["c"]})
    #
    # if len(no_wikipedia) > 5:
    #     no_wikipedia = random.sample(no_wikipedia, 5)

    return render_template('quick_curation.html',
                           #count_no_wikipedia = count_no_wikipedia,
                           no_wikipedia_link_topic = no_wikipedia_link_topic,
                           literal_links = literal_links,
                           formatting = formatting,
                           random = random)

##############################################
@app.route('/field_specific')
def field_specific():
    dir_queries = "./queries"
    ## Get identifiers (hybrid) without a regex (WARNING)
    query = dir_queries + "/no_regex_identifier.rq"
    with open(query, "r") as f:
        query = f.read()
        results = g.query(query)
    f.close()

    no_regex_identifier = []
    for r in results:
        no_regex_identifier.append({"term": r["term"], "class": r["concept"]})


    return render_template('field_specific.html',
                           no_regex_identifier = no_regex_identifier,
                           random = random)



if __name__ == "__main__":
    # context = ('myserver-dev.crt', 'myserver-dev.key')
    # app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
    # context = ('myserver-dev.crt', 'myserver-dev.key')
    app.run(host='0.0.0.0', port=5000, debug=True)