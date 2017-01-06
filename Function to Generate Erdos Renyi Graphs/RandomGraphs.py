#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:31:17 2017

@author: pakinja
"""

from scipy.stats import bernoulli
import networkx as nx
import matplotlib.pyplot as plt


def erdos_graph(N,p):
    """
    Generate an Erdos Renyi Graph.
    """

    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1,node2)
    return G
    

nx.draw(erdos_graph(30, 0.3), node_size= 50, node_color="red")
plt.savefig("graph", figsize=(20,32))