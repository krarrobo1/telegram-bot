from SPARQLWrapper import SPARQLWrapper, JSON
import os

# Load ENV VARS
from dotenv import load_dotenv, find_dotenv
load_dotenv((find_dotenv()))
ONTOLOGY_ENDPOINT = os.getenv('ONTOLOGY_ENDPOINT')

fuseki = SPARQLWrapper(ONTOLOGY_ENDPOINT)
dbpedia = SPARQLWrapper('https://dbpedia.org/sparql')

def get_pizza_list():
    fuseki.setQuery("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX pizza: <http://www.semanticweb.org/pizzatutorial/ontologies/2020/PizzaTutorial#>
    
        SELECT *
        WHERE { ?pizza rdfs:subClassOf pizza:NamedPizza . }
    """)
    fuseki.setReturnFormat(JSON)
    return fuseki.query().convert()

def get_pizzas_info():
    fuseki.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX pizza: <http://www.semanticweb.org/pizzatutorial/ontologies/2020/PizzaTutorial#>
            SELECT ?pizza ?caloricContent ?image ?sp ?mp ?lp (GROUP_CONCAT(?ingredients;SEPARATOR=",") AS ?igroup)
            WHERE {
                  ?pizza rdf:type pizza:SohoPizza . 
                  ?pizza pizza:hasCaloricContent ?caloricContent .
                  ?pizza pizza:hasTopping ?ingredients .
                  OPTIONAL {?pizza pizza:hasImage ?image}
                  OPTIONAL {?pizza pizza:smallPrice ?sp}
                  OPTIONAL {?pizza pizza:mediumPrice ?mp}
                  OPTIONAL {?pizza pizza:largePrice ?lp}
            }
           GROUP BY ?pizza ?caloricContent ?sp ?mp ?lp ?image
        """)
    fuseki.setReturnFormat(JSON)
    return fuseki.query().convert()


def get_pizza_info(choice):
    fuseki.setQuery("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX pizza: <http://www.semanticweb.org/pizzatutorial/ontologies/2020/PizzaTutorial#>
            SELECT ?pizza ?caloricContent ?image ?sp ?mp ?lp (GROUP_CONCAT(?ingredients;SEPARATOR=",") AS ?igroup)
            WHERE {
                  ?pizza rdf:type pizza:"""+choice+""" . 
                  ?pizza pizza:hasCaloricContent ?caloricContent .
                  ?pizza pizza:hasTopping ?ingredients .
                  OPTIONAL {?pizza pizza:hasImage ?image}
                  OPTIONAL {?pizza pizza:smallPrice ?sp}
                  OPTIONAL {?pizza pizza:mediumPrice ?mp}
                  OPTIONAL {?pizza pizza:largePrice ?lp}
            }
        GROUP BY ?pizza ?caloricContent ?image ?sp ?mp ?lp
    
    """)
    fuseki.setReturnFormat(JSON)
    return fuseki.query().convert()