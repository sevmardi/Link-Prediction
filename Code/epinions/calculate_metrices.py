import numpy as np
import networkx as nx
import linkpred
import collections
import pickle
import os

data = np.loadtxt('../../datasets/epinions/out.epinions', dtype = int) # Load the Reality Mining data set
print(data[-1:,:])

data = data[np.where(data[:,0] != data[:,1])] # remove self loops
data = data[:,[0,1,3]]

data = data[data[:,2].argsort()] # sort by timestamp

trainPeriod = data[:588559,:]  
testPeriod = data[588559:,:]


# Convert the periods to undirected graphs.
trainPeriodGraph = nx.Graph(trainPeriod[:,[0,1]].tolist())
testPeriodGraph = nx.Graph(testPeriod[:,[0,1]].tolist())


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

# NMeasure
nmeasure = linkpred.predictors.NMeasure(
    trainPeriodGraph, excluded=trainPeriodGraph.edges())
nmeasure_results = nmeasure.predict()

# Min Overlap
minOverlap = linkpred.predictors.MinOverlap(
    trainPeriodGraph, excluded=trainPeriodGraph.edges())
minOverlap_results = minOverlap.predict()

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
nmeasureList = list(nmeasure_results.values())
minOverlapList = list(minOverlap_results.values())

"""
Save the results.
"""

if not os.path.isdir('epinions_results'):
    os.mkdir('epinions_results')

with open('epinions_results/adamicAdar_epinions.pkl', 'wb') as y:
    pickle.dump(adamicAdarList, y)

with open('epinions_results/commonNeighbors_epinions.pkl', 'wb') as y:
    pickle.dump(commonNeighborsList, y)

with open('epinions_results/rootedPageRankList_epinions.pkl', 'wb') as y:
    pickle.dump(rootedPageRankList, y)

with open('epinions_results/jaccard_epinions.pkl', 'wb') as y:
    pickle.dump(jaccardList, y)

with open('epinions_results/resAllocation_epinions.pkl', 'wb') as y:
    pickle.dump(resAllocationList, y)

with open('epinions_results/assocStrength_epinions.pkl', 'wb') as y:
    pickle.dump(assocStrengthList, y)
    
with open('epinions_results/nmeasure_epinions.pkl', 'wb') as y:
    pickle.dump(nmeasureList, y)
        
with open('epinions_results/minOverlap_epinions.pkl', 'wb') as y:
    pickle.dump(minOverlapList, y)    


# Create a dictionary that represents the testPeriodGraph
testPeriodDict = collections.defaultdict(list)
for node1, node2 in testPeriodGraph.edges():
    testPeriodDict[node1].append(node2)

# Creating the labels (0 or 1). If a pair for which we calculated a metric does not exist in 
# the testing period, it takes a 0, otherwise an 1. The "labels" list will be converted to 
# a column in the pandas data frame later, along with the calculated metrics.
labels = []
datasetPairs = []
for u, v in jaccard_results.keys():   
    datasetPairs.append([u,v])
    if (v in testPeriodDict[u]) or (u in testPeriodDict[v]):
        labels.append(1)
    else:
        labels.append(0)

# Also save the labels
with open('epinions_results/labels_epinions.pkl', 'wb') as y:
    pickle.dump(labels, y)





