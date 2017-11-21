import sys
import csv
import numpy as np
import networkx as nx
from graph_tool.all import *


dublin = 'datasets/Dublin Contacts/ia-contacts_dublin.txt'
digg = 'datasets/digg_networks/out.munmun_digg_reply'

def number_of_edges(graph):
    print('Number of Edges')
    print(str(nx.number_of_edges(graph)))
    print('\n')


def number_of_nodes(graph):
    print("Number of Nodes")
    print(str(nx.number_of_nodes(graph)))
    print('\n')


def pre_processor(filename):
    """
    Create a Di graph. 
    """
    dg = nx.Graph()
    with open(filename, 'r') as files:
        for line in files:
            line = line.rstrip('\n')
            v = line.split(",")
            # v = line.split(" ")

            # dg.add_edge(v[0], v[1], {'weight': v[2], 'timestamp': v[3]})
            dg.add_edge(v[0], v[1], {'timestamp': v[2]})
    print(dg)
    return dg


def main():
    parser = pre_processor(dublin)
    # number_of_nodes(parser)


if __name__ == '__main__':
    main()