from SIR_class import *


class ProblemSIZR(ProblemSIR):
    """docstring for SIZR."""
    def __init__(self, coefs, U0, T, tol=1e-10):

        alfa, beta, delta_S, delta_I, rho, SIGMA = coefs
        if isinstance(alfa, (float, int)):
            self.alfa = lambda t: alfa
        elif callable(alfa):
            self.alfa = alfa

        if isinstance(beta, (float, int)):
            self.beta = lambda t:beta
        elif callable(beta):
            self.beta = beta

        if isinstance(delta_S, (float, int)):
            self.delta_S = lambda t: delta_S
        elif callable(delta_S):
            self.delta_S = delta_S

        if isinstance(delta_I, (float, int)):
            self.delta_I = lambda t: delta_I
        elif callable(delta_I):
            self.delta_I = delta_I

        if isinstance(rho, (float, int)):
            self.rho = lambda t: rho
        elif callable(rho):
            self.rho = rho

        if isinstance(SIGMA, (float, int)):
            self.SIGMA = lambda t:SIGMA
        elif callable(SIGMA):
            self.SIGMA = SIGMA

        self.U0, self.T = U0, T




    def __call__(self, u, t):
        S,I,Z,R = u
        alfa, beta, delta_S, delta_I, rho, SIGMA = self.alfa, self.beta, self.delta_S, self.delta_I, self.rho, self.SIGMA
        dS = SIGMA(t) - beta(t)*S*Z-delta_S(t)*S
        dI = beta(t)*S*Z - rho(t)*I - delta_I(t)*I
        dZ = rho(t)*I - alfa(t)*S*Z
        dR = delta_S(t)*S + delta_I(t)*I + alfa(t)*S*Z
        return [dS, dI, dZ, dR]

# alfa, beta, delta_S, delta_I, rho, SIGMA


if __name__ == "__main__":
    alfa = 0.0016
    beta = 0.0012
    delta_I = 0.014
    delta_S = 0
    SIGMA = 2
    rho = 1
    S0 = 10
    Z0 = 100
    I0 = 0
    R0 = 0
    T = 33 #hours
    dt = 0.5
    U0 = [S0, I0, Z0, R0]
    coefs = [alfa, beta, delta_S, delta_I, rho, SIGMA]
    problem = ProblemSIZR(coefs, U0, T)
    solver = SolverSIR(problem, dt)
    solver.solve(terminate=problem.terminate)
    solver.plot(labels=['S', 'I', 'Z', 'R'], title='SIZR')
    plt.show()

'''
2018.11.18 ZIR> python .\SIZR.py

plots one plott

'''
