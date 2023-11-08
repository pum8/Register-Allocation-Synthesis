import random
from copy import deepcopy

class graphCreater:
    graphSSA = {}
    graphLV = {}
    linkerSSA = {}
    linkerLV = {}
    tempLV = {}
    totalLengthAllLV = 0
    tempFitnessScore = []
    genomeCounter = 0
    BestLIST = []
    density = .5

    def createGraphSSA(self, vertex):
        for each in range(vertex):
            self.graphSSA[each] = []

        for i in range(vertex):
            if i == 0:
                self.addEdge(i, i+1)
                self.addEdge(i, i+2)
            elif i == vertex - 1:
                pass
            elif i == vertex - 1 or i == vertex - 2:
                self.addEdge(i, i+1)
            else:
                self.addEdge(i, i+2)

    def createGraphLVMOD(self, vertex):
        for each in range(vertex):
            self.graphLV[each] = []

        for i in range(int(vertex*self.density)):
            src = random.randrange(0, vertex-1)
            dst = random.choice(self.linkerSSA[src])
            while len(self.graphLV[src]) > 0 or src == dst:
                src = random.randrange(0, vertex-1)
                dst = random.choice(self.linkerSSA[src])
            self.graphLV[src].append(dst)

    def setConnection(self, num, Graph, linkerGraph):
        for each in range(num):
            visited = []
            linkerGraph[each] = self.checkConnection(visited, Graph, each)
            linkerGraph[each].pop(0)

    def checkConnection(self, visited, graph, node):
        if node not in visited:
            visited.append(node)
            for next_node in graph[node]:
                self.checkConnection(visited, graph, next_node)
        return visited

    def addEdge(self, src, dst):
        self.graphSSA[src].append(dst)

    def graphCreation(self, V=None,LVdensity=50):
        if V is None:
            V = random.randrange(10, 20)
        self.density =  float(LVdensity)/100
        self.createGraphSSA(V)
        self.setConnection(V, self.graphSSA, self.linkerSSA)
        self.createGraphLVMOD(V)
        self.setConnection(V, self.graphLV, self.linkerLV)
        print("SSA Graph: ", self.graphSSA)
        print("LV Graph: ", self.graphLV)
        # print("LinkerSSA", self.linkerSSA)
        # print("LinkerLV", self.linkerLV)
        self.tempLV = deepcopy(self.graphLV)