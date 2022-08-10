import numpy as np
from low_pass_filter import low_pass_filter
from high_pass_filter import high_pass_filter

def hp_lp_filtering(ABC_input, neuron_RCs: tuple, dt):
    """
    hp_lp_filtering acts as a high-pass and low-pass filter, reflecting what we see in the fly's brain.
    All the values of time constants RC are taken from table S1 for ON pathway.
    Simulated neurons that perform low-pass filtering: Mi1, Tm3, Mi9.
    """
    # hplp_RC = (mi1_hp_RC, mi1_lp_RC, tm3_hp_RC, tm3_lp_RC, mi9_lp_RC)

    
    ABC_filtered = np.zeros(ABC_input.shape)
    for neuron in range(3):
        if neuron==0 or neuron==1:
            ABC_filtered[neuron, :] = high_pass_filter(ABC_input[neuron, :], dt, neuron_RCs[2*neuron])
            ABC_filtered[neuron, :] = low_pass_filter(ABC_input[neuron, :], dt, neuron_RCs[2*neuron+1])
        elif neuron==2:
            ABC_filtered[neuron,:] = low_pass_filter(ABC_input[neuron, :], dt, neuron_RCs[2*neuron])

    return ABC_filtered