## nQueens
## by Swapnil Lad
## base solution to nQueens problem using Constraint Programming

from ortools.sat.python import cp_model

model = cp_model.CpModel()

#generate the number of queens (should be a term of the dimensional pair of the board)
num_vals = 9

#build into iterable list
list_vals = range(1, 9)

#create decision variables, one for each column, to represent what row corresponds to that column
row = {}
for m in list_vals:
    row[m] = model.NewIntVar(1, num_vals-1, str(m))

#initialize the solver
solver = cp_model.CpSolver()

#assign the constraints to the model
for m in list_vals:
    if (m+1) in list_vals:
        model.Add(row[m] != row[m+1])
        model.Add(row[m] + m != row[m+1] + m + 1)
        model.Add(row[m] - m != row[m+1] - m - 1)
    for n in list_vals:
        if m != n:
            model.Add(row[m] != row[n])

#solve the model
status = solver.Solve(model)

#print model solution
if status == cp_model.OPTIMAL:
    for m in list_vals:
        print("Place Queen %i at (%i, %i)" % (m, m, solver.Value(row[m])))
