import numpy as np

from . import util


class FFTHandler(object):
    """
    The purpose of this class is to compute Fourier transforms of
    simulation data.

    Its methods are very thin wrappers around the underlying numpy
    functions, but it provides a unified interface which also uses
    the naming conventions in the paper ("method 1", "method 2").
    """
    def get_FFT_coeffs_of_average_m(self, m_avg):
        fft_coeffs = np.fft.rfft(m_avg, axis=0)
        return fft_coeffs

    def get_fft_frequencies(self, timesteps, unit='Hz'):
        timestep_unit = util.get_timestep_unit(unit)
        dt = util.convert_to_unit(timesteps[1] - timesteps[0], timestep_unit)

        n = len(timesteps)
        freqs = np.fft.rfftfreq(n, dt)
        # FIXME: We ignore the last element for now so that we can compare with the existing data.
        return freqs[:-1]

    def get_spectrum_via_method_1(self, m_avg):
        """Compute power spectrum from spatially averaged magnetisation dynamics.

        The returned array contains the power spectral densities `S_y(f)` as
        defined in Eq. (1) of the paper.

        Parameters
        ----------
        m_avg :  1D numpy array

            Time series representing dynamics of a single component of
            the spatially averaged magnetisation (for example `m_y`).

        Returns
        -------
        numpy.array

            Power spectral densities of the Fourier-transformed magnetisation data.

        """
        fft_m_avg = self.get_FFT_coeffs_of_average_m(m_avg)
        psd_m_avg = np.abs(fft_m_avg)**2
        # FIXME: We ignore the last element for now so that we can
        #        compare with the existing reference data.
        return psd_m_avg[:-1]
