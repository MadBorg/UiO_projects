def alfa(t):
    if 0<=t<=4:
        return 0
    elif 4<t<=28:
        return 0.0016
    elif 28<t<=33:
        return 0.006

def beta(t):
    if 0<=t<=4:
        return 0.03
    elif 4<t<=28:
        return 0.0012
    elif 28<t<=33:
        return 0

def delta_I(t):
    if 0<=t<=4:
        return 0
    elif 4<t<=28:
        return 0.014
    elif 28<t<=33:
        return 0

def delta_S(t):
    if 0<=t<=4:
        return 0
    elif 4<t<=28:
        return 0
    elif 28<t<=33:
        return 0.0067

def SIGMA(t):
    if 0<=t<=4:
        return 20
    elif 4<t<=28:
        return 2
    elif 28<t<=33:
        return 0
