import numpy as np

class two_phase_simplex():
    '''Two Phase Simplex method operates on linear programs in standard form'''

    def __init__(self):
        self.table = None
        self.RHS = None
        self.var = None
        self.min_max = None
        self.constraint_count = None
        self.list_var = None  
            
    def get_equations(self,user_input):

        # self.min_max = user_input['objective']
        # self.constraint_count = len(user_input['coef_constraints'])
        
        # equations = list()
        # RHS = list()

        # # Get objective function
        # self.var = len(user_input['c_coeff'])

        # equations = np.append(user_input['coef_constraints'], [user_input['c_coeff']], axis=0)
        # user_input['b_value'].append(0)
        # RHS = user_input['b_value']

        # self.table = equations
        # self.RHS = RHS
        # self.list_var = [(x+self.var) for x in range(self.var)]
        
        self.min_max, self.constraint_count = 'MAX', 3
        
        equations = list()
        RHS = list()

        # Get objective function
        self.var = 2r

        equations = [[-1,-1],[-1,1],[1,2],[1,3]]
        RHS = [-3,-1,2,0]

        self.table = equations
        self.RHS = RHS
        self.list_var = [(x+self.var) for x in range(self.constraint_count)]
    def pprint(self, table,list_var,pivot_col,pivot_row):
        '''Pretty print a table to check intermediate results'''
        if(pivot_col != -1):
            print(f"[] Pivoted around "
                                f"{pivot_col, pivot_row}")
        for i in range(len(table[-1]) - 1):
            print ('{:>4}x'.format(i+1),end ='')
        print ('{:>5}'.format('RHS'))        
        print('z  [',end='')
        for j in table[-1]:
            print(str(round(j, 2)) + ' ', end='')
        print(']')
        for i in range(len(table) - 1):
            print('{0}x ['.format(list_var[i] + 1),end='')
            for j in table[i]:
                print(str(round(j, 2)) + ' ', end='')
            print(']')
        print()


    def final_results(self, opt_point):
        '''post-processing of results'''
        # change sign of optimal value if MAX problem
        
        opt_value = self.table[-1][-1]
        
        if self.min_max == 'max':
            opt_value *= -1.0

        # get values of optimal point
        final_opt_pnt = list()
        for i in [0, 1]:
            if i in opt_point:
                final_opt_pnt.append(self.table[opt_point.index(i)][-1])
            else:
                final_opt_pnt.append(0.0)

        return final_opt_pnt, opt_value

    def standard_form(self):
        '''
        Convert the given equations into their standard forms by adding 
        slack variables. Also change sign of optimization function if 
        it is a minimization problem so as to solve for maximization.
        '''
        # add slack variables
        for eq in self.table:
            # zeros = np.zeros(self.constraint_count)  # Array of zeros
            # eq = np.concatenate((eq, zeros))  
            eq.extend([0] * self.constraint_count)
        for i, eq in enumerate(self.table[:-1]):
            if self.RHS[i] < 0:
                eq[i + self.var] = -1
            else:
                eq[i + self.var] = 1

        # convert minimization problem to maximization by changing sign
        self.table = np.array(self.table, dtype=float)
        if self.min_max == 'min':
            self.table[-1] = self.table[-1] * -1 + 0.0

        self.RHS = np.array(self.RHS)
        self.table = np.hstack((self.table, self.RHS[:, np.newaxis]))

    def add_artf(self):
        '''Add artificial variables if there is no initial
        basic feasible solution (BFS)'''
        bfs = True
        for i in range(self.var, self.var + self.constraint_count):
            if np.sum(self.table[:, i]) != 1:
                bfs = False
                art_var = np.zeros((self.constraint_count + 1, 1))
                art_var[i - self.var] = 1.0
                self.table = np.hstack((self.table, art_var))
                self.table[:, (-2, -1)] = self.table[:, (-1, -2)]

        return bfs

    def new_opt_fun(self):
        '''
        Create a new optimization function for the first phase and embed it
        into the table. Also keep track of the position of artificial variables.
        '''
        artf_vars = list()
        for i in range(self.var + self.constraint_count, self.table.shape[1] - 1):
            row_id = np.where(self.table[:, i] < 0)[0]
            if list(row_id):  # NOTE np.array([0]) considered None
                artf_vars.append(self.var + row_id[0])
                self.table[-1][self.var + row_id[0]] = -1
                self.table[-1] += self.table[row_id[0]]

        return artf_vars

    def simplex(self, opt_point):
        '''
        Loop until the optimal point is reached or we get an infeasible solution
        '''

        self.pprint(self.table,self.list_var,-1,-1)
        while not np.all(self.table[-1][:-1] <= 0):
            pivot_col = np.argmax(self.table[-1][:-1])
            # check for feasibility
            if np.all(self.table[:, pivot_col][:-1] <= 0) or \
                    np.any(self.table[:, pivot_col][:-1] == 0) or \
                    np.all(self.table[:, -1][:-1] < 0):
                print('The problem is unbounded')
                exit()
            theta = self.table[:, -1][:-1] / self.table[:, pivot_col][:-1]
            # check for feasibility
            if np.all(theta < 0):
                print('The problem is infeasible')
                exit()
            # set negative ratios to some large number (+ infinity)
            theta[self.table[:, -1][:-1] < 0] = float('inf')
            theta[self.table[:, pivot_col][:-1] < 0] = float('inf')
            # get pivot and convert pivot row to 1 using row operation
            pivot_row = np.argmin(theta)
            self.table[pivot_row] /= self.table[pivot_row][pivot_col]
            # set Identity matrix using row operations
            for i in range(self.constraint_count + 1):
                if i == pivot_row:
                    continue
                self.table[i] = self.table[i]-(self.table[i][pivot_col]/ \
                        self.table[pivot_row][pivot_col])* \
                        self.table[pivot_row]
            self.list_var[pivot_row] = pivot_col
            self.pprint(self.table,self.list_var,pivot_col,pivot_row)
            # keep a record of basic variables
            opt_point[pivot_row] = pivot_col

        return opt_point

    def two_phase(self):
        '''
        Check for initial BFS. If there is an initial BFS, call Simplex else
        save the original OPT function, add artificial variables, get a new OPT
        function, and call the first phase of simplex. If an initial BFS is obtained,
        call the simplex second phase with the original OPT function.
        '''

        # save the original OP function
        Z = self.table[-1]
        bfs = self.add_artf()

        # initial BFS
        init_opt_pt = list(range(self.var, self.var + self.constraint_count))

        # if initial BFS
        if bfs:
            print("\nSimplex Method....")
            opt_point = self.simplex(init_opt_pt)
            return self.final_results(opt_point)

        # if no initial BFS
        # if any RHS is negative, change sign
        neg_RHS = self.table[:, -1] < 0
        self.table[neg_RHS] = self.table[neg_RHS] * -1.0 + 0.0

        # set new OP function with artificial variables
        self.table[-1] = np.zeros(self.table.shape[1])
        artf_vars = self.new_opt_fun()

        # call the first phase
        print("\n1st Phase....")
        opt_point = self.simplex(init_opt_pt)

        # remove artificial variable set original OP function
        self.table = np.delete(self.table, artf_vars, axis=1)
        self.table[-1] = Z

        # check for the identity matrix
        for row, col in enumerate(opt_point):
            self.table[-1] -= self.table[-1][col] * self.table[row]

        # call 2nd phase
        print("\n2nd Phase....")
        opt_point = self.simplex(opt_point)

        return self.final_results(opt_point)
