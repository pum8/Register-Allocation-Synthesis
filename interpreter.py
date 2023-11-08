import CGG
import GraphGeneratorSimple
import ProgramGenerator
from SGA import sga

class interpreter:
    graph = None

    def execute(self,graph, programs):
        self.graph = graph
        self.genomeExecute(programs)
        return self.graph.graphSSA,self.graph.graphLV


    def genomeExecute(self,genome):
        for each in range(len(genome)):
            s = genome[each][0]
            e = genome[each][1]
            p = genome[each][2]
            self.splitLV(s,e,p)
            

    def splitLV(self,src,dst,point):
        if( (dst in self.graph.graphLV[src]) and (point in self.graph.linkerSSA[src]) and  point<dst):
            if(point not in self.graph.graphLV[src]):
                self.graph.graphLV[src].append(point)
                self.graph.graphLV[src].sort()