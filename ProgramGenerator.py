import random 

class ProgramGeneratorOBJ:

    def randomSplitGenerator(self,total,vertex):
        programs = []
        for each in range(total):
            start = random.randrange(0,vertex-1)
            end = random.randrange(0,vertex-1)
            point = random.randrange(0,vertex-1)
            temp= [start,end,point]
            programs.append(temp)
        return programs

    def randomSplitCoalesceGenerator(self,total,vertex):
        programs = []
        for each in range(total):
            src1 = random.randrange(0,vertex-1)
            dst1 = random.randrange(0,vertex-1)
            src2 = random.randrange(0,vertex-1)
            dst2 = random.randrange(0,vertex-1)
            spl_coal = random.randint(1, 2)
            if (spl_coal==1):
                temp= [src1,src2,dst1]
            else:
                temp= [src1,dst1,src2,dst2]
            programs.append(temp)
        return programs

    def randomCoalesceGenerator(self,total,vertex):
        programs = []
        for each in range(total):
            src1 = random.randrange(0,vertex-1)
            dst1 = random.randrange(0,vertex-1)
            src2 = random.randrange(0,vertex-1)
            dst2 = random.randrange(0,vertex-1)

            temp= [src1,dst1,src2,dst2]
            programs.append(temp)
        return programs

    def randomCoalesceGeneratorFixed(self,totalSplit,totalCoalesce,vertex):
        programs = []
        splitPrograms = randomSplitGenerator(totalSplit,vertex)
        coalescePrograms = randomCoalesceGenerator(totalSplit,vertex)
        programs.extend(splitPrograms)
        programs.extend(coalescePrograms)
        
        return programs

