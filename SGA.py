import random 
from copy import deepcopy
import time



class sga:
    graphSSA = {}
    graphLV = {}
    linkerSSA = {}
    linkerLV = {}
    tempLV={}
    totalLengthAllLV=0
    tempFitnessScore = []
    genomeCounter =0
    BestLIST=[]
    baseSplitFunctionNumber = 20
    baseGenomeSize = 20
    incrementGene=10
    genomeList=[]
    node=0
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

    def createGraphLVMOD(self,vertex):   
        for each in range(vertex):
            self.graphLV[each] = []
            
        for i in range(int(vertex/2)):
            src = random.randrange(0,vertex-1)
            dst = random.choice(self.linkerSSA[src])
            while(len(self.graphLV[src])>0 or src==dst):
                src = random.randrange(0,vertex-1)
                #print(graphLV)
                dst = random.choice(self.linkerSSA[src])
            

            self.graphLV[src].append(dst)


    def setConnection(self,num,Graph,linkerGraph):     
        for each in range(num):
            visited =[]
            linkerGraph[each] = self.checkConnection(visited,Graph,each)
            linkerGraph[each].pop(0)


    def checkConnection(self,visited,graph,node):   
        if node not in visited:
            visited.append(node)
            for next in graph[node]:
                self.checkConnection(visited, graph, next)
        return visited


    def addEdge(self,src,dst):
        {
            self.graphSSA[src].append(dst)

        }
    def splitLVtemp(self,src,dst,point):
       if( (dst in self.tempLV[src]) and (point in self.linkerSSA[src]) and  point<dst):
          if(point not in self.tempLV[src] and point in self.lengthLV(self.graphSSA,src,self.graphLV[src][0])):
                self.tempLV[src].append(point)
                self.tempLV[src].sort()
                print("inside split",src,dst,point)
    def lengthLV(self,graph, start, end, path=[]):

        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        length = None
        for node in graph[start]:
            if node not in path:
                newpath = self.lengthLV(graph, node, end, path)
                if newpath:
                    if not length or len(newpath) < len(length):
                        length = newpath
        return length


    def lengthTotalLV(self):
        total= 0
        for each in range(0,len(self.graphLV)):
            if not self.graphLV[each]:
                pass
            else:
                total += len(self.lengthLV(self.graphSSA,each,self.graphLV[each][0]))-1

        
        return total
    def fitnessScore(self,graphMeasure):
        totalNumberLV = 0

        for each in graphMeasure:
            totalNumberLV+= len(graphMeasure[each])


        ft = totalNumberLV/self.totalLengthAllLV
    
        return ft
    def randomSplitGenerator(self,total,vertex):
        gene = []
        for each in range(total):
            start = random.randrange(0,vertex-1)
            end = random.randrange(0,vertex-1)
            point = random.randrange(0,vertex-1)
            temp= [start,end,point]
            gene.append(temp)
        return gene

    def genomeExecute(self,genome):
        for each in range(len(genome)):
            s = genome[each][0]
            e = genome[each][1]
            p = genome[each][2]
            self.splitLVtemp(s,e,p)
    def geneticAlgorithm(self):
    
        for each in range(self.baseGenomeSize):
            self.genomeList.append([])
            
        
        for each in range(self.baseGenomeSize):
            temp = self.randomSplitGenerator(self.baseSplitFunctionNumber,self.V)
            #print(temp,"\n")
            self.genomeList[each].append(temp)

        for each in self.genomeList: # execute the genomes
            for i in each:
                self.genomeExecute(i)
    def GA(self):

        global tempLV
        print("GraphLV",self.graphLV)
        print("tempLV",self.tempLV)

        for each in range(self.baseGenomeSize):
            self.genomeList.append([])

        for each in range(self.baseGenomeSize):
            temp = self.randomSplitGenerator(self.baseSplitFunctionNumber,self.node)
            #print(temp,"\n")
            self.genomeList[each].append(temp)

        for each in self.genomeList: # execute the genomes
            for i in each:
                self.genomeExecute(i)
                
            self.tempFitnessScore.append(self.fitnessScore(self.tempLV))
            tempLV=deepcopy(self.graphLV)
        
        #global genomeCounter
        self.genomeCounter +=1
        print("Genome Counter: ", self.genomeCounter)

    def crossOverNMutate(self,listCrossOver):
        crossed=[]
        for each in range(0,(int(len(listCrossOver)/2))):


            first=random.choice(listCrossOver[0])
            second=random.choice(listCrossOver[0])
            point=random.randrange(1,self.baseGenomeSize-1)

            new=[first[:point]+second[point:]]
            
            start = random.randrange(0,self.node-1)
            end = random.randrange(0,self.node-1)
            point = random.randrange(0,self.node-1)
            temp= [start,end,point]
            
            new[0][0]=temp
            crossed.append(new)
        return crossed

    def main(self):
        V = random.randrange(10,20)
        self.node = V
        self.createGraphSSA(V)
        self.setConnection(V,self.graphSSA,self.linkerSSA)
        self.createGraphLVMOD(V)
        self.setConnection(V,self.graphLV,self.linkerLV)
        print("SSA Graph: ",self.graphSSA)
        print("LV Graph: ",self.graphLV)
        #print("LinkerSSA",linkerSSA)
        #print("LinkerLV",linkerLV)
        self.tempLV=deepcopy(self.graphLV)
        self.totalLengthAllLV = self.lengthTotalLV()
        print(self.totalLengthAllLV) 
        print(self.graphLV)
        baseSplitFunctionNumber = 20
        baseGenomeSize = 20
        incrementGene=10
        genomeList=[]
        self.GA()
        while(1 not in self.tempFitnessScore):
            bestSplitFunctions=[]
            newTempFitnessScore=[]
            for each in range(0,int(len(self.tempFitnessScore)/2)):
                tempMax =max(self.tempFitnessScore)
                index=self.tempFitnessScore.index(tempMax)
                bestSplitFunctions.append(self.genomeList[index])
                newTempFitnessScore.append(tempMax)
                self.tempFitnessScore.remove(tempMax)

            tempFitnessScore=newTempFitnessScore #Doubt
            genomeList=bestSplitFunctions
            
            genomeList=self.crossOverNMutate(bestSplitFunctions)

            
            listLengthPreviousGenomeList=len(genomeList)
            for each in range(len(genomeList),incrementGene+len(genomeList)):
                genomeList.append([])

            for each in range(listLengthPreviousGenomeList,incrementGene+listLengthPreviousGenomeList):
                temp = self.randomSplitGenerator(baseSplitFunctionNumber,self.node)
                genomeList[each].append(temp)
            tempFitnessScore=[]
            for each in genomeList: # execute the genomes

                for i in each:
                    
                    self.genomeExecute(i)
                tempFitnessScore.append(self.fitnessScore(self.tempLV))
                
            self.tempLV=deepcopy(self.graphLV)

            
            if(self.genomeCounter==500):
                break
            
            self.genomeCounter +=1
            print("genome Counter \n",self.genomeCounter)
            
            
            BestLIST=genomeList

            
            if(self.genomeCounter%10==0):
                incrementGene +=5
            
            if(self.genomeCounter%100==0):
                time.sleep(5)


            print("This is max FT: \n",max(tempFitnessScore))

            for each in BestLIST: # execute the genomes

                for i in each:
                    
                    self.genomeExecute(i)
                tempFitnessScore.append(self.fitnessScore(self.tempLV))
        #print(self.tempLV)
        #print(self.graphSSA)
        return [self.graphSSA,self.tempLV,self.graphLV]



