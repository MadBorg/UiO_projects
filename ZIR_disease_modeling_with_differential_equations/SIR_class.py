
import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class ProblemSIR(object):
    import numpy as np
    import matplotlib.pyplot as plt
    import ODESolver

    def __init__(self, beta, nu, U0, T, tol=1e-10):
        '''
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulation for t in [0,T]
        '''
        self.U0 = U0
        #self.S0, self.I0, self.R0 = S0, I0, R0
        self.T = T

        if isinstance(nu, (float, int)): #number?
            self.nu =lambda t: nu #wrap as function
        elif callable(nu):
            self.nu = nu
        #else:
        #    print('Error in init: self.nu')

        if isinstance(beta, (float, int)): #number?
            self.beta =lambda t: beta #wrap as function
        elif callable(beta):
            self.beta = beta
        #else:
        #    print('Error in init: self.beta')

    def terminate(self, u, t, step_no):
        tol = self.tol
        return abs(sum(u[step_no])-sum(self.U0)) > tol



    def __call__(self, u, t):
        beta, nu, U0 = self.beta, self.nu, self.U0
        S, I, R = u
        return [-beta(t) *S*I, beta(t)*S*I - nu(t)*I, nu(t)*I]

    def terminate(self, u, t, step_no, tol=1e-10):
        return abs(sum(u[step_no])-sum(self.U0)) > tol
        #return False #True

class SolverSIR(object):
    import ODESolver
    import numpy as np
    import matplotlib.pyplot as plt
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODESolver.RungeKutta4,terminate=None):
        self.solver = method(self.problem)
        ic = self.problem.U0
        #ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        self.u, self.t = self.solver.solve(t)
        return [self.u,self.t]
        #self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def plot(self,labels=None, title=None, xlabel=None, ylabel=None, colors=None):
        #S,I,R = self.S, self.I, self.R
        u = self.u
        t = self.t
        #plt.plot(t, S, 'k-', t, I, 'b-', t, R, 'r-')
        if type(colors) is list:
            plt.plot(t,u,colors)
        else:
            plt.plot(t,u)
        if type(labels) is list:
            plt.legend(labels, loc = 'lower right')
        else:
            plt.legend()

        plt.gca().set_title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        #plt.show()

if __name__ == "__main__":

    def beta(t):
        if 0 <= t <= 12:
            return 0.0005
        if t > 12:
            return 0.0001

    beta2 = 0.0005
    #beta = lambda t: 0.0005 if 0<=t<=12 else 0.0001 if t>12
    dt = 0.1
    nu = 0.1
    U0 = [S0, I0, R0] = [1500, 1, 0]
    T = 60 #days


    plt.subplot(1,2,1)
    problemb1 = ProblemSIR(beta, nu, U0, T)
    solverb1 = SolverSIR(problemb1,dt)
    solverb1.solve(terminate=problemb1.terminate)
    solverb1.plot(labels=['S','I','R'], title='beta(t)', colors=['g', 'r', 'b'])


    plt.subplot(1,2,2)
    problemb2 = ProblemSIR(beta2, nu, U0, T)
    solverb2 = SolverSIR(problemb2,dt)
    solverb2.solve(terminate=problemb2.terminate)
    solverb2.plot(labels=['S','I','R'], title='beta2= 0.0005', colors=['g', 'r', 'b'])

    plt.show()

'''
2018.11.18 ZIR> python .\SIR_class.py

#plots 2 plots named beta2 = 0.0005 and beta(t)
'''
