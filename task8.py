from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

rain, hagrid, dumbledore = symbols('rain hagrid dumbledore')

# If not rain then visited Hagrid
imp1 = Implies(Not(rain), hagrid)
# Either visited Hagrid or Dumbledore (exclusive not required here)
either = Or(hagrid, dumbledore)
# Suppose we assert Harry visited Dumbledore today
kb = And(imp1, either, dumbledore)

print("Knowledge base:", kb)

# Check if KB & rain is satisfiable (i.e., is there a model where it's true)
sat_models = satisfiable(kb & rain, all_models=True)
print("Satisfiable models for (KB and rain)?")
for m in sat_models:
    print(m)
