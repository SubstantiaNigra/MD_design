from scipy.ndimage import gaussian_filter1d
import numpy as np


def photoreceptor_input_filtering(VF, deg_sep: int, azim_n: int, elev_n: int, stim_t: int, N: int):
    """
    photoreceptor_input filters the visual field VF and averages it over time. 
    It filters the signal with 1D Gaussian Filter 
    with distance deg_sep [degree] between each photoreceptos every t_res [ms].
    It averages the signal (simple mean) over N time-steps leaving (stim_t-1) values for each pixel.
    """
    sigma = int(np.floor(deg_sep / 2)) # it tells how many pixels before the peak are taken for filtering
    first_peak: int = int(np.ceil(deg_sep / 2)) # it tells the position of the first peak and how many pixels after the peak
                                                # are taken into consideration

    photoreceptor_input = np.zeros(VF.shape)
    for t_step in range(stim_t):
        for row in range(azim_n):
            for column in range(first_peak-1, elev_n, first_peak):
                VF_column = VF[row, column-sigma:column+first_peak, t_step] # take a columns for filtering
                photoreceptor_input[row, column-sigma:column+first_peak, t_step] = gaussian_filter1d(VF_column, 
                                                                                                    sigma=sigma, axis=0, order=2)
    
    
    avg_ph_input = np.zeros(((elev_n, azim_n, stim_t-1)))
    for t_step in range(0,stim_t-1):
        pixel_to_average = photoreceptor_input[:,:,t_step:t_step+N]
        avg_ph_input[:, :, t_step] = np.mean(pixel_to_average, axis=2)
    
    
    return avg_ph_input
