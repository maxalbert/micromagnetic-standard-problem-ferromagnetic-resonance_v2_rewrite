import numpy as np


class FFTHandler(object):
    """
    The purpose of this class is to compute Fourier transforms of
    simulation data.

    Its methods are very thin wrappers around the underlying numpy
    functions, but it provides a unified interface which also uses
    the naming conventions in the paper ("method 1", "method 2").
    """
    def __init__(self, data_reader):
        self.data_reader = data_reader

    def get_FFT_coeffs_of_average_m(self, component):
        m_vals = self.data_reader.get_average_magnetisation(component)
        fft_coeffs = np.fft.rfft(m_vals, axis=0)
        return fft_coeffs

    def get_fft_frequencies(self, unit='Hz'):
        if unit == 'Hz':
            timestep_unit = 's'
        elif unit == 'GHz':
            timestep_unit = 'ns'
        else:
            raise ValueError("Invalid unit: '{}'. Allowed values: 's', 'ns'")

        n = self.data_reader.get_num_timesteps()
        dt = self.data_reader.get_dt(unit=timestep_unit)
        freqs = np.fft.rfftfreq(n, dt)
        # FIXME: We ignore the last element for now so that we can compare with the existing data.
        return freqs[:-1]

    def get_spectrum_via_method_1(self, component):
        """Compute power spectrum from spatially averaged magnetisation dynamics.

        The returned array contains the power spectral densities `S_y(f)` as
        defined in Eq. (1) of the paper.

        Parameters
        ----------
        data_avg :  1D numpy array

            Time series representing dynamics of a single component
            of the spatially averaged magnetisation (e.g. `m_y`).

        dt :  float

            Size of the timestep at which the magnetisation was sampled
            during the simulation (e.g. `dt=5e-12` for every 5 ps).

        Returns
        -------
        Pair of `numpy.array`s

            Frequencies and power spectral densities of the magnetisation
            data. Note that the frequencies are returned in GHz (not Hz).
        """
        fft_data_avg = self.get_FFT_coeffs_of_average_m(component)
        psd_data_avg = np.abs(fft_data_avg)**2
        # FIXME: We ignore the last element for now so that we can compare with the existing data.
        return psd_data_avg[:-1]
