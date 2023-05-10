from typing import List

import numpy as np

from .exceptions import InfeasibleProblem
from .exceptions import ReachedOptimality
from .exceptions import UnboundedProblem


class Tableau:
    """
    `Simplex Tableau` contains and performs basic operations such as pivoting
    on the problem data.

    There is one primary use case for this class, which is employed by the
    `Solver` class:

    1. Intialize Tableau (see `__init__()`) with program data in **standard
       form**.
    2. Open Tableau as a Context Manager and operate on it using the
       `pivot()` method.
    3. The pivot method will raise an exception once a termination point
       has been reached (optimality, unboundedness, or infeasibility).
    4. Extract Tableau data by directly accessing its attributes (see
       below).

    Attributes
    ----------
    obj_value : float
       linear program objective value, arbitrary if problem is unbounded
    solution : List[float]
       solution to the linear program, if any.
    basis : List[float]
       indices of the basis matrix.


    Methods
    -------
    pivot(use_blands_rule=False)
        determines entering and departing variables and pivots tableau.
    """


    def __init__(self, obj_func: List[float], coeffs: List[List[float]], constraints: List[float]):
        """
        Creates tableau object `(self.tab)` from program data in **standard
        form**.

        Parameters
        ----------
        obj_func: values af the objective function, in order. Must be of
           size *n* (n = number of variables).
        coeffs: values of technological coefficients (params), row-major.
          Must be size *m x n* (m = number of constraints)
        constraints: values of the contraint column-vector (right-hand
        side). Must be size *m*.
        """
        # calculate reduced costs
        self.obj_func = obj_func
        obj_func = [-v for v in obj_func]

        # tableau object is a single large m + 1 x n + 1 matrix
        obj_value = 0
        self.tab = np.r_[
            np.r_[obj_func, obj_value][np.newaxis, :],
            np.c_[coeffs, constraints]]

        # float type is necessary for future conversions
        self.tab = self.tab.astype(float)

        # useful for calculations (m, n)
        self.shape = (len(constraints), len(obj_func))

        # state of tableau (None, Optimal, Unbounded, or Infeasible)
        self.state = None

    def __repr__(self):
        """
        Returns string representation of tableau.
        """

        # Suppress scientific notation and convert tableau to string
        with np.printoptions(suppress=True):
            # Convert tableau to string
            top = np.arange(1, self.tab.shape[1] + 1)
            top[-1] = -1  # Used as a placeholder
            tab = np.r_[top[np.newaxis, :], self.tab]
            rows = str(tab).split('\n')

        # Strip off extra bracket off last row
        rows[-1] = rows[-1][:-1]

        # Top row with variables
        top = "     " + rows[0].replace('.', 'x').replace('-1x', 'RHS')[2:-1]

        # Add basis variables
        return '\n'.join([top] + [f'{f"x{var + 1}" if var != "" else "z "} {row}'
                                  for row, var in zip(rows[1:], [''] + self.basis)])


    def __enter__(self):
        """ Enter method for context manager. Returns self."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Exit method for context manager. """

        # if context exits without an exception (no solution found)
        if not exc_type:
            return

        try:
            # exception is mapped to the following states
            self.state = {
                ReachedOptimality: "Optimal",
                UnboundedProblem: "Unbounded",
                InfeasibleProblem: "Infeasible"
            }[exc_type]
        except KeyError:
            # if it is another exception, let it be raised
            return False
        return True

    @property
    def obj_value(self) -> float:
        """
        Returns the objective value.
        """
        return self.tab[0][-1]

    @property
    def solution(self) -> List[float]:
        """
        Returns the solution vector.
        """
        return self.tab[1:, -1]

    @property
    def basis(self) -> List[float]:
        """
        Returns indices of basis vector.

        Looks for each basic vector in the tableau, and stores index in
        the basis. -1 is stored in the absence of a corresponding basis
        column.
        """

        # Identity shifted over so top row is zeroes
        identity = np.identity(self.shape[0] + 1)[1:]

        # Default basis has all -1's
        basis = np.full(self.shape[0], -1)

        # Find matching columns in identity matrix and tableau
        for i, row in enumerate(identity):
            matching_columns = np.all(self.tab.T == row, axis=1)
            matching_indices = np.where(matching_columns)[0]

            # Store index of the first matching column, if any
            if matching_indices.size > 0:
                basis[i] = matching_indices[0]

        return list(basis)


    def pivot(self, use_blands_rule=False):
        """
        Calculates departing and entering variables and calls
        `_pivot_around()`. Raises exception upon termination condition.

        Raises
        ------
        ReachedOptimality
           If optimality conditions have been reached.
        InfeasibleProblem
           If problem is feasible and unable to pivot.
        UnboundedProblem
           If problem is unbounded.
        """

        tab_0, tab_1, tab_minus1 = self.tab[0], self.tab[1:], self.tab[:, -1]
        entering_var_candidates = np.argwhere(tab_0[:-1] < 0)

        if entering_var_candidates.size == 0:
            feasible_sol = np.all(tab_1[:, -1] >= 0)
            raise ReachedOptimality if feasible_sol else InfeasibleProblem

        entering_var = (entering_var_candidates.min() if use_blands_rule
                        else tab_0[:-1].argmin())

        col = tab_1[:, entering_var]
        positive_col_indices = col > 0
        ratios = np.divide(tab_1[:, -1], col,
                           out=np.full(col.shape, np.inf, dtype=float),
                           where=positive_col_indices)
        departing_var = ratios.argmin()

        if not use_blands_rule or not positive_col_indices[departing_var]:
            raise UnboundedProblem

        if use_blands_rule:
            val = ratios[departing_var]
            basis_array = np.array(self.basis)
            departing_var = self.basis.index(np.min(basis_array[ratios == val]))

        self.pivot_idx = (departing_var + 1, entering_var)
        self._pivot_around(*self.pivot_idx)


    def _pivot_around(self, r: int, c: int) -> None:
        
        # r : index of departing variable
        # c : index of entering variable
        
        # Indices are relative to the tableau; they are not the constraint or variable indices.

        # divide row by pivot
        self.tab[r] /= self.tab[r, c]

        # zero out column, except for pivot
        mask = np.ones(self.tab.shape[0], dtype=bool)
        mask[r] = False
        self.tab[mask] -= self.tab[r] * self.tab[mask, c][:, np.newaxis]
    
    def add_artificial_variables(self):
        # Inserts artificial columns in tableau and calculates new reduce costs.

        # calculate new reduced costs
        new_basic_cost = -(np.array(self.basis) == -1).astype(int)
        self.tab[0] = np.dot(new_basic_cost, self.tab[:, 1:])

        # add artificial variable columns
        args = np.where(self.basis == -1)[0]
        identity = np.eye(self.shape[0])
        self.artificial_vars = np.arange(self.shape[1], self.shape[1] + len(args))
        self.tab = np.insert(self.tab, self.tab.shape[1]-1, identity[args], axis=1)

    def drop_artificial_variables(self):
        """
        Removes artificial variables that have been driven out of the
        basis.

        Raises
        ------
        InfeasibleProblem
            if artificial variable is in basis with positive value

        Returns
        -------
        Function does not return anything.
        """

        # check basis for artificial vars
        artificial_vars_mask = np.in1d(self.basis, self.artificial_vars)
        if np.any(artificial_vars_mask & (self.tab[:, -1] > 0)):
            raise InfeasibleProblem

        # drop artificial variables
        self.tab = np.delete(self.tab, self.artificial_vars, axis=1)

        # calculate new costs
        costs = self.obj_func[self.basis]
        self.tab[0] = np.dot(costs, self.tab[:, 1:]) - self.tab[-1, :]
