import pickle

with open('MathOverflow/adamicAdar_MathOverflow.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('MathOverflow/commonNeighbors_MathOverflow.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('MathOverflow/rootedPageRankList_MathOverflow.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('MathOverflow/jaccard_MathOverflow.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('MathOverflow/resAllocation_MathOverflow.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('MathOverflow/assocStrength_MathOverflow.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)