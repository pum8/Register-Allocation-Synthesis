#!/usr/bin/env python
# coding: utf-8

import random 
from copy import deepcopy
import time
import sys

graphSSA = {}
graphLV = {}
linkerSSA = {}
linkerLV = {}
tempLV = {}
totalLengthAllLV = 0
tempFitnessScore = []
genomeCounter = 0
BestLIST = []
LVPercent = 0.0

def createGraphSSA(vertex): 
    graphSSA[0] = []
    graphSSA[1] = []
    addEdge(0, 1)
    for i in range(2, vertex):
        random_node = random.choice(list(graphSSA.keys()))
        while(len(graphSSA[random_node]) >= 2):
            random_node = random.choice(list(graphSSA.keys()))

        graphSSA[i] = []
        addEdge(random_node, i)

def createGraphLVMOD(vertex):  
    for each in range(vertex):
        graphLV[each] = []
        
    for i in range(int(vertex * LVPercent)):
        src = random.randrange(0, vertex - 1)
        while(len(linkerSSA[src]) == 0):
            src = random.randrange(0, vertex - 1)
        if(len(linkerSSA[src]) > 0):
            dst = random.choice(linkerSSA[src])
              
        while (len(graphLV[src]) > 0 or src == dst or len(linkerSSA[src]) == 0):
            src = random.randrange(0, vertex - 1)
            if(len(linkerSSA[src]) > 0):
                dst = random.choice(linkerSSA[src])
        
        graphLV[src].append(dst)

def setConnection(num, Graph, linkerGraph):      
    for each in range(num):
        visited = []
        linkerGraph[each] = checkConnection(visited, Graph, each)
        linkerGraph[each].pop(0)

def checkConnection(visited, graph, node):    
    if node not in visited:
        visited.append(node)
        for next_node in graph[node]:
            checkConnection(visited, graph, next_node)
    return visited

def addEdge(src, dst):
    graphSSA[src].append(dst)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python CGG.py <number_of_nodes> <live_range_density>")
        sys.exit(1)

    userInput = int(sys.argv[1])
    LVPercent = float(sys.argv[2])/100

    createGraphSSA(userInput)
    setConnection(userInput, graphSSA, linkerSSA)
    print("SSA Graph: ", graphSSA)

    createGraphLVMOD(userInput)
    setConnection(userInput, graphLV, linkerLV)
    print("LV Graph: ", graphLV)
