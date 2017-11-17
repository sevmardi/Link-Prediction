import pickle
import pandas as pd
"""
Read the metrics.

"""

with open('UC-Irvine/adamicAdar_UC-Irvine.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('UC-Irvine/commonNeighbors_UC-Irvine.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('UC-Irvine/rootedPageRankList_UC-Irvine.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('UC-Irvine/jaccard_UC-Irvine.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('UC-Irvine/resAllocation_UC-Irvine.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('UC-Irvine/assocStrength_UC-Irvine.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)
    
with open('UC-Irvine/labels_UC-Irvine.pkl', 'rb') as y:
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