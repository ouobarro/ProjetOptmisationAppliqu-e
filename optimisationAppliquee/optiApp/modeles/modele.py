import minizinc
from minizinc import Instance, Model, Solver
import os

def resolutionContrainte(modelPath,DataPath):
    module_dir = os.path.dirname(__file__)  
    modeleFile = os.path.join(module_dir, modelPath)
    modelData= os.path.join(module_dir, DataPath)
    model = Model(str(modeleFile))
    model.add_file(str(modelData))
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, model)
    result = instance.solve(all_solutions=True)
    print(result)
    result_to_str=""
    for i in range(len(result)):
        result_to_str+=str(result[i,"_output_item"]+"\n\n")
    return result_to_str

#print("pour le trio\n")

#resolutionContrainte("projetTrioMusicien.mzn","projetTrioMusicien.dzn")
#print("pour le duo\n")
#resolutionContrainte("projetDuoMusicien.mzn","projetDuoMusicien.dzn")