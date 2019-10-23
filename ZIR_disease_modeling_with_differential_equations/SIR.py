import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class Logistic:
    def __init__(self, beta, nu, U0):
        self.beta, self.nu, self.U0 = beta, nu, U0

    def __call__(self, u, t):
        beta, nu, U0 = self.beta, self.nu, self.U0
        S, I, R = u
        return [-beta *S*I, beta*S*I - nu*I, nu*I]

    def terminate(self, u, t, step_no, tol=1e-10):
        return abs(sum(u[step_no])-sum(self.U0)) > tol
        #return False #True

dt = 0.5
nu = 0.1
days = 60 #for days >= 12 RuntimeWarning: overflow encountered in double_scalars; return [-beta1 *S*I, beta1*t*S*I - nu*I, nu*R]
n = int(days+1)
beta = [float(1e-4*5),float(1e-4)]

#beta1, beta2 = float(1e-4*5),float(1e-4)
t = np.linspace(0, days, n+1) #days
S = np.zeros(n+1);I = np.zeros(n+1);R = np.zeros(n+1)
S0, I0, R0 = 1500, 1, 0
S[0] = 1500; I[0] = 1; R[0] = 0
U0 = [S0, I0, R0]

c = 0 #counter
for b in beta:
    c += 1
    f = Logistic(b, nu, U0)
    solver = ODESolver.ForwardEuler(f)
    solver.set_initial_condition(U0)
    u, t = solver.solve(t, f.terminate)
    plt.subplot(1,len(beta),c)
    plt.gca().set_title("SIR, with b={}".format(b))
    plt.plot(t,u)
    plt.legend(['S', 'I', 'R'], loc = 'lower right')
    plt.xlabel('days')
plt.show()


'''
når vi kjører med en mindre beta så stiger (-beta *S*I) den derriverte av S.
Så da tar det legngere tid å bli infisert

2018.11.18 ZIR> python .\SIR.py

 #plotter 2 subplot med forksjellige betta verdier

'''
