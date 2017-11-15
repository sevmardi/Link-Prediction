import numpy as np
import networkx as nx
import linkpred
import collections

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

data = np.loadtxt('RealityMining.txt',dtype = int) # Load the Reality Mining data set
data = data[:,[0,1,3]] # We don't need the weight column

# The data set is sorted by timestamp. We extract rows from 1 to 900.000 to indicate the train period.
# The rest indicate the test period
trainPeriod = data[:900000,:]  
testPeriod = data[900000:,:]

# Convert the periods to undirected graphs.
trainPeriodGraph = nx.Graph(trainPeriod[:,[0,1]].tolist())
testPeriodGraph = nx.Graph(testPeriod[:,[0,1]].tolist())

# Don't mind this for now.
#p = linkpred.predictors.base.Predictor(trainPeriodGraph)
#l = p.likely_pairs(k = 2)
#trainPeriodNeighbors = nx.Graph(l) 

# Compute the Adamic Adar measure. This function finds for each node its 2-size neighborhood and
# calculates the measure for all pairs of nodes in the 2-size neighborhood. 
# It excludes the nodes that belong in the train period by using the 'excluded' argument
adamicAdar = linkpred.predictors.AdamicAdar(trainPeriodGraph, excluded = trainPeriodGraph.edges())
adamicAdar_results = adamicAdar.predict()

# commonNeighbors measure
commonNeighbors = linkpred.predictors.CommonNeighbours(trainPeriodGraph, excluded = trainPeriodGraph.edges())
commonNeighbors_results = commonNeighbors.predict(alpha = 0)

# converting the metrics into lists. We will feed them into pandas data frames later
adamicAdarList = list(adamicAdar_results.values())
commonNeighbors = list(commonNeighbors_results.values())

# Create a dictionary that represents the testPeriodGraph
testPeriodDict = collections.defaultdict(list)
for node1, node2 in testPeriodGraph.edges():
    testPeriodDict[node1].append(node2)

# Creating the labels (0 or 1). If a pair for which we calculated a metric does not exist in 
# the testing period, it takes a 0, otherwise an 1. The "labels" list will be converted to 
# a column in the pandas data frame later, along with the calculated metrics.
labels = []
for u, v in adamicAdar_results.keys():   
    if (v in testPeriodDict[u]) or (u in testPeriodDict[v]):
        labels.append(1)
    else:
        labels.append(0)

























