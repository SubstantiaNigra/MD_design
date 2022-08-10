import numpy as np

def low_pass_filter(x, dt, RC):
    """
    Return RC low-pass filter output samples y, given input samples x,
    time interval dt, and time constant RC
    """
    n = len(x)
    y = np.zeros(x.shape)

    alfa = dt / (RC + dt)
    y[0] = alfa * x[0]

    for i in range(1,n):
        y[i] = alfa * x[i] + (1-alfa) * y[i-1]
    return y