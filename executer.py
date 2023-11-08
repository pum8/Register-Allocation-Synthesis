from GraphGeneratorSimple import graphCreater
from ProgramGenerator import ProgramGeneratorOBJ
from CGG import Generator
from SGA import sga
from interpreter import interpreter


graph_generator = graphCreater()
graph_generator.graphCreation(10,50)

print("linkerLV ",graph_generator.linkerLV)
print("linkerSSA ",graph_generator.linkerSSA)

GG = Generator()
GG.graphCreation(10,50)
print("linkerLV ",GG.linkerLV)
print("linkerSSA ",GG.linkerSSA)



program_generator = ProgramGeneratorOBJ()

split_programs = program_generator.randomSplitGenerator(10,10)
print("split programs ",split_programs)


SSA,LV = interpreter().execute(graph_generator,split_programs)
print("SSA, LV : ",SSA,LV)

SSA,LV = interpreter().execute(GG,split_programs)
print("SSA, LV : ",SSA,LV)



