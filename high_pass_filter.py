import numpy as np

def high_pass_filter(x, dt, RC):
    """
    Return RC high-pass filter output samples, given input samples,
    time interval dt, and time constant RC
    """
    n = len(x)
    y = np.zeros(x.shape)
    
    alfa = RC / (RC + dt)
    y[1] = x[1]
    for i in range(2, n):
        y[i] = alfa * y[i-1] + alfa * (x[i] - x[i-1])
    return y