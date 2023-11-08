#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
from copy import deepcopy
import time

graphSSA = {}
graphLV = {}
linkerSSA = {}
linkerLV = {}
tempLV={}
totalLengthAllLV=0
tempFitnessScore = []
genomeCounter =0
BestLIST=[]

def createGraphSSA(vertex) :
    
    for each in range(vertex):
       graphSSA[each] = []

    for i in range(vertex):
        if(i == 0):
            addEdge(i,i+1)
            addEdge(i,i+2)
            
        elif(i==V-1):
            pass
        elif(i== vertex-1 or i== vertex-2):
            addEdge(i,i+1)
        else:
            addEdge(i,i+2)

def createGraphLVMOD(vertex):   
    for each in range(vertex):
        graphLV[each] = []
        
    for i in range(int(vertex/2)):
        src = random.randrange(0,vertex-1)
        dst = random.choice(linkerSSA[src])
        while(len(graphLV[src])>0 or src==dst):
            src = random.randrange(0,vertex-1)
            #print(graphLV)
            dst = random.choice(linkerSSA[src])
        

        graphLV[src].append(dst)


def setConnection(num,Graph,linkerGraph):     
    for each in range(num):
        visited =[]
        linkerGraph[each] = checkConnection(visited,Graph,each)
        linkerGraph[each].pop(0)


def checkConnection(visited,graph,node):   
    if node not in visited:
        visited.append(node)
        for next in graph[node]:
            checkConnection(visited, graph, next)
    return visited


def addEdge(src,dst):
    {
        graphSSA[src].append(dst)

    }
     


V = random.randrange(10,20)
createGraphSSA(V)
setConnection(V,graphSSA,linkerSSA)
createGraphLVMOD(V)
setConnection(V,graphLV,linkerLV)
print("SSA Graph: ",graphSSA)
print("LV Graph: ",graphLV)
print("LinkerSSA",linkerSSA)
print("LinkerLV",linkerLV)
tempLV=deepcopy(graphLV)





def splitLVtemp(src,dst,point):
    
    if( (dst in tempLV[src]) and (point in linkerSSA[src]) and  point<dst):
        if(point not in tempLV[src] and point in lengthLV(graphSSA,src,graphLV[src][0])):
            tempLV[src].append(point)
            tempLV[src].sort()
            print("inside split",src,dst,point)
    


print(graphLV)





def lengthLV(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    length = None
    for node in graph[start]:
        if node not in path:
            newpath = lengthLV(graph, node, end, path)
            if newpath:
                if not length or len(newpath) < len(length):
                    length = newpath
    return length


def lengthTotalLV():
    total= 0
    for each in range(0,len(graphLV)):
        if not graphLV[each]:
            pass
        else:
            total += len(lengthLV(graphSSA,each,graphLV[each][0]))-1

    
    return total
            
totalLengthAllLV = lengthTotalLV()
print(totalLengthAllLV) 
print(graphLV)

def fitnessScore(graphMeasure):
    totalNumberLV = 0

    for each in graphMeasure:
        totalNumberLV+= len(graphMeasure[each])


    ft = totalNumberLV/totalLengthAllLV
  
    return ft


print(graphLV)





"""baseSplitNumber = 50
nextGenesNumber = 10
newSplitNumber = 5"""

def randomSplitGenerator(total,vertex):
    gene = []
    for each in range(total):
        start = random.randrange(0,vertex-1)
        end = random.randrange(0,vertex-1)
        point = random.randrange(0,vertex-1)
        temp= [start,end,point]
        gene.append(temp)
    return gene

def genomeExecute(genome):
    for each in range(len(genome)):
        s = genome[each][0]
        e = genome[each][1]
        p = genome[each][2]
        splitLVtemp(s,e,p)
        
    
    
    
    






baseSplitFunctionNumber = 20
baseGenomeSize = 20
incrementGene=10


genomeList=[]

def geneticAlgorithm():
   
    for each in range(baseGenomeSize):
        genomeList.append([])
        
    
    for each in range(baseGenomeSize):
        temp = randomSplitGenerator(baseSplitFunctionNumber,V)
        #print(temp,"\n")
        genomeList[each].append(temp)

    for each in genomeList: # execute the genomes
        for i in each:
            genomeExecute(i)
    



def GA():

    global tempLV
    print("GraphLV",graphLV)
    print("tempLV",tempLV)

    for each in range(baseGenomeSize):
        genomeList.append([])

    for each in range(baseGenomeSize):
        temp = randomSplitGenerator(baseSplitFunctionNumber,V)
        #print(temp,"\n")
        genomeList[each].append(temp)

    for each in genomeList: # execute the genomes
        for i in each:
            genomeExecute(i)
            
        tempFitnessScore.append(fitnessScore(tempLV))
        tempLV=deepcopy(graphLV)
    
    global genomeCounter
    genomeCounter +=1
    print("Genome Counter: ", genomeCounter)

        
            
            




def crossOverNMutate(listCrossOver):
    crossed=[]
    for each in range(0,(int(len(listCrossOver)/2))):


        first=random.choice(listCrossOver[0])
        second=random.choice(listCrossOver[0])
        point=random.randrange(1,baseGenomeSize-1)

        new=[first[:point]+second[point:]]
        
        start = random.randrange(0,V-1)
        end = random.randrange(0,V-1)
        point = random.randrange(0,V-1)
        temp= [start,end,point]
        
        new[0][0]=temp
        crossed.append(new)
    return crossed


GA()
while(1 not in tempFitnessScore):
    bestSplitFunctions=[]
    newTempFitnessScore=[]
    for each in range(0,int(len(tempFitnessScore)/2)):
        tempMax =max(tempFitnessScore)
        index=tempFitnessScore.index(tempMax)
        bestSplitFunctions.append(genomeList[index])
        newTempFitnessScore.append(tempMax)
        tempFitnessScore.remove(tempMax)

    tempFitnessScore=newTempFitnessScore #Doubt
    genomeList=bestSplitFunctions
    
    genomeList=crossOverNMutate(bestSplitFunctions)

    
    listLengthPreviousGenomeList=len(genomeList)
    for each in range(len(genomeList),incrementGene+len(genomeList)):
        genomeList.append([])

    for each in range(listLengthPreviousGenomeList,incrementGene+listLengthPreviousGenomeList):
        temp = randomSplitGenerator(baseSplitFunctionNumber,V)
        genomeList[each].append(temp)
    tempFitnessScore=[]
    for each in genomeList: # execute the genomes

        for i in each:
            
            genomeExecute(i)
        tempFitnessScore.append(fitnessScore(tempLV))
        
    tempLV=deepcopy(graphLV)

    
    if(genomeCounter==500):
        break
    
    genomeCounter +=1
    print("genome Counter \n",genomeCounter)
    
    
    BestLIST=genomeList

    
    if(genomeCounter%10==0):
        incrementGene +=5
    
    if(genomeCounter%100==0):
        time.sleep(5)


    print("This is max FT: \n",max(tempFitnessScore))
    














fitnessScore(graphLV)
#print(tempFitnessScore)




for each in BestLIST: # execute the genomes

    for i in each:
        
        genomeExecute(i)
    tempFitnessScore.append(fitnessScore(tempLV))
print(tempLV)
print(graphSSA)







