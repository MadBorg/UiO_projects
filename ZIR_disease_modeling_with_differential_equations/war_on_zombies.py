from SIZR import *
import numpy as np
import matplotlib.pyplot as plt

S0 = 50
Z0 = 3

beta = 0.03
alfaBase = 0.2*beta
a =  50*alfaBase
T_angrep= [5,10,18]
sigma = 0.5
delta_I = delta_S = SIGMA = 0
rho = 1
T = 20
dt = 0.1
class alfaLogistic():
    def __init__(self,alfaBase, sigma, T_angrep):
        self.sigma, self.T_angrep = sigma, T_angrep
        self.m = len(T_angrep)
        self.a = 50*alfaBase
        self.alfa =lambda t: alfaBase

    def __call__(self, t):
        return self.alfa(t) + self.omega(t, self.T_angrep)

    def omega(self, t, T):
        O = self.a
        S = 0
        for i in range(self.m):
            S += np.exp(-1/2 *((t-T[i])**2/self.sigma))
        return O * S

if __name__ == "__main__":
    U0 = [S0, I0, Z0, R0] = [50, 0, 3, 0]
    alfa = alfaLogistic(alfaBase, sigma, T_angrep)
    coefs = [alfa, beta, delta_S, delta_I, rho, SIGMA]
    problem = ProblemSIZR(coefs, U0, T)
    solver = SolverSIR(problem, dt)
    solver.solve(terminate=problem.terminate)
    solver.plot(labels=['S', 'I', 'Z', 'R'], title='SIZR')
    plt.show()
'''
The plot shows that the human race persists.

2018.11.18 ZIR> python .\war_on_zombies.py
plots one plot

'''
