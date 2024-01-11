from pyomo.environ import ConcreteModel, Var, Objective, Param, RangeSet, minimize

def OF(model, t, s):
    return model.P[t, s] * model.x[t, s] + model.y[t, s]

model = ConcreteModel()

# Define sets
model.T = RangeSet(1, 24)
model.S = RangeSet(1, 4)

# Define decision variables
model.x = Var(model.T, model.S, domain=range(10))
model.y = Var(model.T, model.S, domain=range(10))

# Define parameter
model.P = Param(model.T, model.S, initialize={ (t, s): 1.0 for t in model.T for s in model.S })

# Add objectives
for t in model.T:
    for s in model.S:
        model.add_component(
            f"obj_{t, s}",
            Objective(
                rule=lambda m, t=t, s=s: OF(m, t, s),
                sense=minimize
            )
        )