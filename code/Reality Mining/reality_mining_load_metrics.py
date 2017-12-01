import pickle
import pandas as pd

"""
Read the metrics.

"""
    
with open('reality_mining/adamicAdar_reality_mining.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('reality_mining/commonNeighbors_reality_mining.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('reality_mining/rootedPageRankList_reality_mining.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('reality_mining/jaccard_reality_mining.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('reality_mining/resAllocation_reality_mining.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('reality_mining/assocStrength_reality_mining.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)
   
with open('reality_mining/labels_reality_mining.pkl', 'rb') as y:
    labels = pickle.load(y)
    
labels2 = []
for el in labels:
    if el == 1:
        labels2.append("yes")
    else:
        labels2.append("no")

dataset = pd.DataFrame(
    {'Adamic Adar': adamicAdarList,
     'Common Neighbors': commonNeighborsList,
     'Rooted PageRank': rootedPageRankList,
     'Jaccard': jaccardList,
     'Resource Allocation': resAllocationList,
     'Association Strength': assocStrengthList,
     'Labels': labels2,
    })        
        