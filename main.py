import minizinc
from minizinc import Instance, Model, Solver

model = Model("projetTrioMusicien.mzn")
model.add_file("projetTrioMusicien.dzn")
gecode = Solver.lookup("gecode")
instance = Instance(gecode, model)
result = instance.solve()

print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
