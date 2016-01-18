import numpy as np


def make_magnetisation_precession(num_timesteps, num_oscillations):
    """
    Construct an artificial magnetisation precession with a simple FFT transform.
    This precession is a pure cosine wave with `num_oscillations` oscillations.

    Returns a pair `(timesteps, m)` where:

    `timesteps` is a 1D array of length `num_timesteps` representing timesteps
    between 0 and 20 ns.

    `m` is a 1D array containing the artificial magnetisation precession values
    at these timesteps.

    """
    timesteps = np.linspace(5e-12, 20e-9, num_timesteps)
    amplitude = 1. / (num_timesteps // 2)
    m = amplitude * np.cos(num_oscillations * (2*np.pi) * timesteps / max(timesteps))

    return timesteps, m
