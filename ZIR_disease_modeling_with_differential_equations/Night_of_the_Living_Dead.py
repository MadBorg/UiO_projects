from SIZR import *
import numpy as np

alfa = np.vectorize(lambda t: 0 if 0 <= t <= 4 else (0.0016 if 4 < t <= 28 else 0.006))
beta = np.vectorize(lambda t: 0.03 if 0 <= t <= 4 else (0.0012 if 4 < t <= 28 else 0))
delta_I = np.vectorize(lambda t: 0 if 0 <= t <= 4 else (0.014 if 4 < t <= 28 else 0))
delta_S = np.vectorize(lambda t: 0 if 0 <= t <= 4 else (0.014 if 4 < t <= 28 else 0))
SIGMA = np.vectorize(lambda t: 20 if 0 <= t <= 4 else (3 if 4 < t <= 28 else 0))
S0 = 60
I0 = 0
Z0 = 1
R0 = 0
T = 33
dt = 0.5
rho = 1 #rho = lambda t: 1
coefs = [alfa, beta, delta_S, delta_I, rho, SIGMA]
U0 = [S0, I0, Z0, R0]
if __name__ == "__main__":
    problem = ProblemSIZR(coefs, U0, T)#init the problem
    solver = SolverSIR(problem, dt)#choose the solver class and enter the problem
    solver.solve(terminate=problem.terminate)#solve the problem, with a terminate function.
    solver.plot(labels=['S', 'I', 'Z', 'R'], title='SIZR')
    plt.show()

'''
2018.11.18 ZIR> python Night_of_the_Living_Dead.py

#plots one plott
'''
