from simplex_method.solver import SimplexSolver
from simplex_method.two_phase_simplex import two_phase_simplex
from standard_form import standard_form
from test_cases import user_inputs

if __name__ == '__main__':
    
    user_inputs = user_inputs[8]
    # if any(x < 0 for x in user_inputs['b_value']):

    #     # initialize object
    #     simx = two_phase_simplex()

    #     # get equations and standardize them
    #     simx.get_equations(user_inputs)
    #     simx.standard_form()

    #     # call the two-phase simplex method
    #     opt_point, opt_value = simx.two_phase()

    #     # print results
    #     print('\nOutput:\n')
    #     print('Optimal point is {}'.format(opt_point))
    #     print('Optimal value is {}'.format(opt_value))
    # else:
    problem=standard_form(user_inputs) 
    
    problem['obj_func']*= -1
    
    check_min = 1
    if user_inputs['objective'] == 'min':
        check_min = -1
    
    use_blands_rule = False

    
    if (any(x == 0 for x in problem['constraints'])):
        use_blands_rule = True
    # initialize solver
    solver = SimplexSolver(obj_func=problem['obj_func'],
                    coeffs=problem['coeffs'],
                    constraints=problem['constraints'])
    # run solver
    print("Beginning solve...\n")
    sol = solver.solve(use_blands_rule=use_blands_rule,
                    print_tableau=True, 
                    No_var = problem['No_var'],
                    check_min = check_min, 
                    var_none = problem['var_none'],
                    list_Var_positive = problem['list_Var_positive'],)
    print('\n', sol)
