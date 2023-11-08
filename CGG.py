import random 
from copy import deepcopy
import time
import sys

class Generator():    
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
    def createGraphSSA(self, vertex):
            self.graphSSA[0] = []
            self.graphSSA[1] = []
            self.addEdge(0, 1)
            for i in range(2, vertex):
                random_node = random.choice(list(self.graphSSA.keys()))
                while len(self.graphSSA[random_node]) >= 2:
                    random_node = random.choice(list(self.graphSSA.keys()))
                self.graphSSA[i] = []
                self.addEdge(random_node, i)

    def createGraphLVMOD(self, vertex):
        for each in range(vertex):
            self.graphLV[each] = []

        for i in range(int(vertex * self.LVPercent)):
            src = random.randrange(0, vertex - 1)
            while len(self.linkerSSA[src]) == 0:
                src = random.randrange(0, vertex - 1)
            if len(self.linkerSSA[src]) > 0:
                dst = random.choice(self.linkerSSA[src])

            while (len(self.graphLV[src]) > 0 or src == dst or len(self.linkerSSA[src]) == 0):
                src = random.randrange(0, vertex - 1)
                if len(self.linkerSSA[src]) > 0:
                    dst = random.choice(self.linkerSSA[src])

            self.graphLV[src].append(dst)

    def setConnection(self, num, graph, linkerGraph):
        for each in range(num):
            visited = []
            linkerGraph[each] = self.checkConnection(visited, graph, each)
            linkerGraph[each].pop(0)

    def checkConnection(self, visited, graph, node):
        if node not in visited:
            visited.append(node)
            for next_node in graph[node]:
                self.checkConnection(visited, graph, next_node)
        return visited

    def addEdge(self, src, dst):
        self.graphSSA[src].append(dst)



    def graphCreation(self,V=None,LV=50):
        if V is None:
            V = random.randrange(10, 20)

        self.LVPercent = float(LV)/100
        self.createGraphSSA(V)
        self.setConnection(V, self.graphSSA, self.linkerSSA)
        self.createGraphLVMOD(V)
        self.setConnection(V, self.graphLV, self.linkerLV)
        print("SSA Graph: ", self.graphSSA)
        print("LV Graph: ", self.graphLV)
        # print("LinkerSSA", self.linkerSSA)
        # print("LinkerLV", self.linkerLV)
        self.tempLV = deepcopy(self.graphLV)