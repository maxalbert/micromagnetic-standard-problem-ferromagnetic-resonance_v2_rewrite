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

    def _get_FFT_coeffs_of_average_m(self, m_avg):
        fft_coeffs = np.fft.rfft(m_avg, axis=0)
        return fft_coeffs

    def get_fft_frequencies(self, timesteps, unit='Hz'):
        """
        Return the FFT sample frequencies for the given timesteps.

        The argument `unit` determines the unit of the returned
        frequencies. It can be either 'Hz' or 'GHz'.

        Note: The timesteps passed into this function must be given
              in units of second (not nanosecond)!
        """
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
        fft_m_avg = self._get_FFT_coeffs_of_average_m(m_avg)
        psd_m_avg = np.abs(fft_m_avg)**2
        # FIXME: We ignore the last element for now so that we can
        #        compare with the existing reference data.
        return psd_m_avg[:-1]

    def get_spectrum_via_method_2(self, m_vals):
        r"""Compute power spectrum from spatially resolved magnetisation dynamics.

        The returned array contains the power spectral densities `\tilde{S}_y(f)`
        as defined in Eq. (5) of the paper.

        Parameters
        ----------
        m_vals :  2D or 3D numpy array

            Time series representing dynamics of a single component of
            the spatially resolved magnetisation, sampled on a regular
            grid. It is assumed that time is along the first dimension.
            That is, `data[k, i, j]` contains the magnetisation at
            timestep `t_k` for the grid point `r_{i,j}`.

        dt :  float

            Size of the timestep at which the magnetisation was sampled
            during the simulation (e.g. `dt=5e-12` for every 5 ps).

        Returns
        -------
        Pair of `numpy.array`s

            Frequencies and power spectral densities of the magnetisation
            data. Note that the frequencies are returned in GHz (not Hz).
        """

        assert m_vals.ndim == 3

        N, nx, ny = m_vals.shape
        m_vals = m_vals.reshape(N, -1)

        fft_data_full = np.fft.rfft(m_vals, axis=0)
        psd_data_full = np.abs(fft_data_full)**2
        psd_data_avg = np.mean(psd_data_full, axis=1)
        # FIXME: We ignore the last element for now so that we can compare with the existing data.
        return psd_data_avg[:-1]
