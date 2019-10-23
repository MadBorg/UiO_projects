import ODESolver
from SIR_class import *
import numpy as np
import matplotlib.pyplot as plt


class ProblemSIRV(ProblemSIR):
    def __init__(self, beta, nu, p, U0, T):
        ProblemSIR.__init__(self, beta, nu, U0, T)
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

    def __call__(self, u, t):
        beta, nu, p, U0 = self.beta, self.nu,self.p, self.U0
        S, I, R, V = u
        return [-beta(t)*S*I - p(t)*S, beta(t)*S*I - nu(t)*I, nu(t)*I, p(t)*S]

dt = 0.1
nu = 0.1
beta = 0.0005
p = 0.1
U0 = [S0, I0, R0, V0] = [1500, 1, 0, 0]
T = 60 #days

if __name__ == "__main__":
    problem = ProblemSIRV(beta, nu, p, U0, T)
    solver = SolverSIR(problem, dt)
    solver.solve(terminate=problem.terminate)
    solver.plot(labels=['S', 'I', 'R', 'V'], title='SIRV', colors=['b', 'r','g','y'], xlabel='days')
    plt.show()

'''
Effekten er tydelig. I har bare et lite hopp så tar vkasinasjonen over.
Og ikke mange rekker å bli infisert. Vaksinen er dermed svert effektiv

2018.11.18 ZIR> python .\SIRV.py

pots one plot
'''
