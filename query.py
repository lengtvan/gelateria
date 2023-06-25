from rdflib import *
# Load the ontology and data into an RDF graph
graph = Graph()
graph.parse("/Users/rmit/Downloads/Yummy/gelatontology.owl", format="xml")

# Define the ontology namespace
gelateria = Namespace("http://gelatontology.com/#")

# Define the SPARQL query
query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    SELECT ?nutrient
    WHERE {
                gelateria:hasNutrient ?nutrient .
    }
"""

# Execute the SPARQL query
results = graph.query(query, initNs={"gelateria": gelateria})

# Process the query results
for row in results:
    gelato = row["gelato"]
    nutrient = row["nutrient"]
    print(f"Gelato: {gelato}, Nutrient: {nutrient}")