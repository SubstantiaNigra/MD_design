import numpy as np

def visual_field(azim_n: int, elev_n: int, stim_t: int, stim_w: int, v: int):
    """
    This function creates the visual field, ie., the input to the motion detector.
    azim_n: number of pixels in azimuthal direction
    elev_n: number of pixels in elevation direction
    stim_t: duration of stimulus
    stim_w: width of stimulus
    v: velocity of the stimulus [pixels / 10ms]=[how many pixels to the right the stimulus 
        moves for each time step, ie. 10ms]
    """

    VF = np.zeros((elev_n, azim_n, stim_t))
    stimulus = np.ones((azim_n,stim_w))


    VF[:,0:stim_w,0] = stimulus
    VF_to_roll = VF[:,:,0]
    for i in range(1, stim_t):
        VF_to_roll = np.roll(VF_to_roll, v) # shift the stimulus by one pixel column
        VF[:, :, i] = VF_to_roll

    # # gratings - a different way to create a grid
    # x = np.arange(-500, 501, 1)

    # X, Y = np.meshgrid(x, x)

    # wavelength = 200
    # grating = np.sin(2 * np.pi * X / wavelength)

    # plt.set_cmap("gray")
    # plt.imshow(grating)
    # plt.show()


    return VF