from SIRV import *


def p(t):
    if 6 <= t <= 15:
        return 0.1
    else:
        return 0

if __name__ == "__main__":
    problem = ProblemSIRV(beta, nu, p, U0, T)
    solver = SolverSIR(problem, dt)
    u ,t= solver.solve(terminate=problem.terminate)
    solver.plot(labels=['S', 'I', 'R', 'V'], title='SIRV', colors=['b', 'r','g','y'], xlabel='days')
    plt.show()

'''
2018.11.18 ZIR> python .\SIRV_varying_p.py

plots one plot
'''
