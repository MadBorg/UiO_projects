from SIRV import *

p = lambda t: 0.1 if 6<= t <=6+VT else 0



def maxI(VT):
    p = lambda t: 0.1 if 6<= t <=6+VT else 0
    problem = ProblemSIRV(beta, nu, p, U0, T)
    solver = SolverSIR(problem, dt)
    u ,t= solver.solve(terminate=problem.terminate)
    return max(u[:,2])


if __name__ == "__main__":
    n = 32
    VT = np.linspace(0,31,n)
    y = np.zeros(n)
    for i in range(len(VT)):
        y[i] = maxI(VT[i])
    plt.plot(VT, y)
    plt.show()

'''


'''
