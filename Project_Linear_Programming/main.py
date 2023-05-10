from simplex_method.solver import SimplexSolver

problem ={
    'obj_func': [4,5,0,0,0],
    'coeffs': [
        [2,2,1,0,0],
        [1,0,0,1,0],
        [0,1,0,0,1]
    ],
    'constraints': [9,4,3],
    'No_var': 2,
}

problem ={
    'obj_func': [1, 0, 0],
    'coeffs': [
        [1, 1, 0],
        [-1, 0, 1]
    ],
    'constraints': [-1, -1],
    'solution': None,
    'No_var': 2,
}
# problem ={
#     'obj_func': [3,1,0,0,0,0],
#     'coeffs': [
#         [1,2,0,1,0,0],
#         [1,1,-1,0,1,0],
#         [7,3,-5,0,0,1]
#     ],
#     'constraints': [5,2,20],
#     'No_var': 3
# }

# initialize solver
solver = SimplexSolver(obj_func=problem['obj_func'],
                       coeffs=problem['coeffs'],
                       constraints=problem['constraints'])
# run solver
print("Beginning solve...\n")
sol = solver.solve(use_blands_rule=True,
                   print_tableau=True, No_var = problem['No_var'])

print('\n', sol)
