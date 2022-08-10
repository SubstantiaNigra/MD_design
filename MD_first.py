import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
from matplotlib import colors
import time
from visual_field import visual_field
from photoreceptor_input_filtering import photoreceptor_input_filtering
from sample_input import sample_input
from hp_lp_filtering import hp_lp_filtering

def RF_1D(phi, sigma_cen, sigma_sur, A_cen, A_sur):

    x = 0.5 * (phi / sigma_cen)**2
    gauss1 = np.exp(-x)
    
    A_rel = A_sur / A_cen
    y = 0.5 * (phi / sigma_sur)**2
    gauss2 = A_rel * np.exp(-y)

    rf = gauss1 - gauss2

    return rf


def create_grid():
    # create discrete colormap
    cmap = colors.ListedColormap(['black', 'white'])
    bounds = [0,1]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    return cmap, norm

def show_VF(VF, n_a, n_e, cmap, norm):
    """
    show_VF simply shows the grid-like pattern, ie., the visual field of the fly.
    """
    fig, ax = plt.subplots()
    ax.imshow(VF, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(0, n_a, 1));
    ax.set_yticks(np.arange(0, n_e, 1));
    





t: int = 120 # [ms]
dt = 10
n_a: int = 90 # [degree]
n_e: int = 90 # [degree]
w: int = 24 # [degree] width of stimulus in the Visual Field
v:int = 1


t_res: int = 10 # [ms] time resolution = every 10ms pixels from VF are sampled
N = 12 # how many time-samples to average over
deg_sep: int = 5 # offset of input lines
first_peak: int = int(np.ceil(deg_sep)-1) # technically, first peak is in the 3rd column, but for Python it's 3-1 = 2 position in VF

vf = visual_field(n_a, n_e, stim_t=t, stim_w=w, v=v) # get visual field [rows, cols, time]
vf_filtered = photoreceptor_input_filtering(vf, deg_sep, n_a, n_e, stim_t=t, N=N) # filter the VF with Gaussian filter and average over time
sampled_input = sample_input(vf_filtered=vf_filtered, deg_sep=deg_sep, first_peak=first_peak, n_a=n_a) # sample filtered inputs [A, B, C...]

mi1_hp_RC, mi1_lp_RC = 1078, 266 # RC high-pass and low-pass filter time constant[ms]
tm3_hp_RC, tm3_lp_RC = 1769, 158 # [ms]
mi9_lp_RC = 546 # [ms]
neuron_RCs = (mi1_hp_RC, mi1_lp_RC, tm3_hp_RC, tm3_lp_RC, mi9_lp_RC)

ABC_input = sampled_input[20, 0:3, :] # just a single detector
ABC_filtered = hp_lp_filtering(ABC_input=ABC_input, neuron_RCs=neuron_RCs, dt=dt)

A = ABC_input[0, :]
B = ABC_input[1, :]
C = ABC_input[2, :]
pd = (A * B) / (C +0.1)

# plt.subplot(311)
# plt.figure(0)
# way = 2
# plt.plot(ABC_input[way, :])
# plt.subplot(312)
# plt.plot(ABC_filtered[way, :], 'r')
# plt.subplot(313)

# cmap, norm = create_grid()
# for i in range(3):

# for i in range(60):
#     show_VF(vf[:,:,i], n_a=n_a, n_e=n_e, cmap=cmap, norm=norm)
#     plt.show()
    # time.sleep(1)
    

plt.figure()
plt.plot(pd)



plt.show()