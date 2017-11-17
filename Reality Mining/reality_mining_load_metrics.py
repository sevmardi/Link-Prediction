import pickle
import pandas as pd

"""
Read the metrics.

"""
    
with open('Reality Mining/adamicAdar_reality_mining.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('Reality Mining/commonNeighbors_reality_mining.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('Reality Mining/rootedPageRankList_reality_mining.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('Reality Mining/jaccard_reality_mining.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('Reality Mining/resAllocation_reality_mining.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('Reality Mining/assocStrength_reality_mining.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)
   
with open('Reality Mining/labels_reality_mining.pkl', 'rb') as y:
    labels = pickle.load(y)
    
dataset = pd.DataFrame(
    {'Adamic Adar': adamicAdarList,
     'Common Neighbors': commonNeighborsList,
     'Rooted PageRank': rootedPageRankList,
     'Jaccard': jaccardList,
     'Resource Allocation': resAllocationList,
     'Association Strength': assocStrengthList,
     'Labels': labels,
    })
3