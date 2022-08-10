import numpy as np

def sample_input(vf_filtered, deg_sep, first_peak, n_a):
    """
    photoreceptor_input samples the filtered Visual Field (filtered by photoreceptor_input_filtering())
    by taking VF input pixel separated deg_sep [degree] from each other
    """
    return vf_filtered[:, 0:n_a:deg_sep, :]