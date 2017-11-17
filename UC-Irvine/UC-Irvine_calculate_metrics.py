import numpy as np
import networkx as nx
import linkpred
import collections
import pickle
import os

"""
The linkpred module makes it (relatively) easy to calculate the metrics we want, without explicitly creating 
the train and test sets. For example, the function 

linkpred.predictors.AdamicAdar(trainPeriodGraph, excluded = trainPeriodGraph.edges())

will calculate the AdamicAdar metric for the 2-size neighborhood (all the combinations of nodes that 
are 2 steps away from each other) of the specified "training graph", by excluding all the pairs that
belong to the "training graph". The "training graph" is the graph of the "training period" we have
specified.

The disadvantage is that linkpred is relatively slow for networks with a lot of edges. The good thing is
that when we calculate a measure, we can then save it into a file and load it when needed.
"""

data = np.loadtxt('UC-Irvine/UC-Irvine.txt',dtype = int)
data = data[:,[0,1,3]] # We don't need the weight column

# The data set is sorted by timestamp. We extract rows from 1 to 48000 to indicate the train period.
# The rest indicate the test period
trainPeriod = data[:48000,:]  
testPeriod = data[48000:,:]

# Convert the periods to undirected graphs.
trainPeriodGraph = nx.Graph(trainPeriod[:,[0,1]].tolist())
testPeriodGraph = nx.Graph(testPeriod[:,[0,1]].tolist())

"""
A different way to extract the 2-size neighborhood.
Don't mind this for now.
"""
#p = linkpred.predictors.base.Predictor(trainPeriodGraph)
#l = p.likely_pairs(k = 2)
#trainPeriodNeighbors = nx.Graph(l) 

"""
Calculate metrics for each node and its 2-size neighborhood. The functions exclude the nodes
that belong in the train period ('excluded' argument).

Some of those measures will be very slow for large networks, due to nested for loops.
"""

# Adamic Adar
adamicAdar = linkpred.predictors.AdamicAdar(trainPeriodGraph, excluded = trainPeriodGraph.edges())
adamicAdar_results = adamicAdar.predict()

# commonNeighbors measure
commonNeighbors = linkpred.predictors.CommonNeighbours(trainPeriodGraph, excluded = trainPeriodGraph.edges())
commonNeighbors_results = commonNeighbors.predict(alpha = 0)

# Rooted PageRank
rootedPageRank = linkpred.predictors.RootedPageRank(trainPeriodGraph, excluded = trainPeriodGraph.edges())
rootedPageRank_results = rootedPageRank.predict(weight = None, k = 2)

# Jaccard coefficient
jaccard = linkpred.predictors.Jaccard(trainPeriodGraph, excluded = trainPeriodGraph.edges())
jaccard_results = jaccard.predict()

""" 
The pearson coefficient does not produce the same amount of rows as a result (for some reason).
Do not calculate for now.
"""
# Pearson coefficient
#pearson = linkpred.predictors.Pearson(trainPeriodGraph, excluded = trainPeriodGraph.edges())
#pearson_results = pearson.predict()

# Resource Allocation
resAllocation = linkpred.predictors.ResourceAllocation(trainPeriodGraph, excluded = trainPeriodGraph.edges())
resAllocation_results = resAllocation.predict()

# Association Strength
assocStrength = linkpred.predictors.AssociationStrength(trainPeriodGraph, excluded = trainPeriodGraph.edges())
assocStrength_results = assocStrength.predict()

# converting the metrics into lists. We will feed them into pandas data frames later
adamicAdarList = list(adamicAdar_results.values())
commonNeighborsList = list(commonNeighbors_results.values())
rootedPageRankList = list(rootedPageRank_results.values())
jaccardList = list(jaccard_results.values())
#pearsonList = list(pearson_results.values())
resAllocationList = list(resAllocation_results.values())
assocStrengthList = list(assocStrength_results.values())

"""
Save the metrics.
"""

if not os.path.isdir('UC-Irvine'):
    os.mkdir('UC-Irvine')

with open('UC-Irvine/adamicAdar_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(adamicAdarList, y)

with open('UC-Irvine/commonNeighbors_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(commonNeighborsList, y)

with open('UC-Irvine/rootedPageRankList_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(rootedPageRankList, y)

with open('UC-Irvine/jaccard_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(jaccardList, y)

with open('UC-Irvine/resAllocation_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(resAllocationList, y)

with open('UC-Irvine/assocStrength_UC-Irvine.pkl', 'wb') as y:
    pickle.dump(assocStrengthList, y)

# Create a dictionary that represents the testPeriodGraph
testPeriodDict = collections.defaultdict(list)
for node1, node2 in testPeriodGraph.edges():
    testPeriodDict[node1].append(node2)

# Creating the labels (0 or 1). If a pair for which we calculated a metric does not exist in 
# the testing period, it takes a 0, otherwise an 1. The "labels" list will be converted to 
# a column in the pandas data frame later, along with the calculated metrics.
labels = []
datasetPairs = []
for u, v in adamicAdar_results.keys():   
    datasetPairs.append([u,v])
    if (v in testPeriodDict[u]) or (u in testPeriodDict[v]):
        labels.append(1)
    else:
        labels.append(0)


























