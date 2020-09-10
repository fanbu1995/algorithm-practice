#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:17:18 2020

@author: fan
"""

#%% practice graph algorithms

from math import inf

class graph:
    def __init__(self, V, E):
        #self.V = V
        self.G = [[0 for v in V] for v in V]
        for i,j,d in E:
            self.G[V.index(i)][V.index(j)] = d
        self.V = list(range(len(V)))
        
    def printDistance(self, src, dist):
        print('Distance from source node {}:'.format(src))
        for v in self.V:
            print(v,dist[v])
        return
    
    def minDist(self, dist, included):
        """
        find the vertex v that 
        1) is not in included, and
        2) has shortest distance to the origin
        """
        mindist = inf
        
        for v in self.V:
            if included[v]==False and dist[v] < mindist:
                min_vertex = v
                mindist = dist[v]
                
        return min_vertex
    
    def dijkstra(self, src):
        
        # initialize distances from source
        dist = [inf for v in self.V]
        dist[src] = 0
        
        # initialize included set
        included = [False for v in self.V]
        
        for i in range(len(self.V)):
            # need to go through all nodes
            
            u = self.minDist(dist, included)
            included[u] = True
            
            for v in self.V:
                if self.G[u][v] > 0 and included[v]==False and dist[u]+self.G[u][v] < dist[v]:
                    dist[v] = dist[u]+self.G[u][v]
                    
        return dist

#%% try it out
V = [1,2,3,4,5]
E = [[1,2,7],
     [2,4,3],
     [4,5,6],
     [5,3,3],
     [1,3,99]]
g = graph(V,E)
dist = g.dijkstra(0) 
g.printDistance(0,dist)            
            