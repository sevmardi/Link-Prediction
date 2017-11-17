import pickle

"""
Read the metrics.

"""

with open('/UC-Irvine/adamicAdar_UC-Irvine.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('/UC-Irvine/commonNeighbors_UC-Irvine.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('/UC-Irvine/rootedPageRankList_UC-Irvine.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('/UC-Irvine/jaccard_UC-Irvine.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('/UC-Irvine/resAllocation_UC-Irvine.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('/UC-Irvine/assocStrength_UC-Irvine.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)