from __future__ import division
import numpy as np
import os
import unittest

from postprocessing import FFTHandler


class TestFFTHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Create an instance of `FFTHandler` which can be re-used for each test.
        """
        cls.fft_handler = FFTHandler()

    def test__get_fft_frequencies(self):
        """
        FFTHandler.get_fft_frequencies() returns expected frequencies of power spectrum.
        """

        timesteps = np.linspace(5e-12, 20e-9, 4000)
        fft_freqs_expected = np.linspace(0, 100e9, 2000, endpoint=False)
        fft_freqs_GHz_expected = np.linspace(0, 100, 2000, endpoint=False)

        fft_freqs = self.fft_handler.get_fft_frequencies(timesteps)
        fft_freqs_GHz = self.fft_handler.get_fft_frequencies(timesteps, unit='GHz')

        self.assertTrue(np.allclose(fft_freqs, fft_freqs_expected, atol=0, rtol=1e-13))
        self.assertTrue(np.allclose(fft_freqs_GHz, fft_freqs_GHz_expected, atol=0, rtol=1e-13))

    def test__get_spectrum_via_method_1_returns_array_of_expected_shape(self):
        """
        FFTHandler.get_spectrum_via_method_1() returns expected result for a known signal.
        """

        fft_handler = FFTHandler()

        num_timesteps = 4000
        num_oscillations = 3
        TOL = 1e-14

        # Construct an artificial magnetisation precession with known FFT transform.
        # This precession is a pure cosine wave with a few oscillations.
        timesteps = np.linspace(5e-12, 20e-9, num_timesteps)
        amplitude = 1. / (num_timesteps // 2)
        m_avg_y = amplitude * np.cos(num_oscillations * (2*np.pi) * timesteps / max(timesteps))

        # Compute the FFT transform and check that the resulting FFT coefficients are as expected:
        #
        # (i) The single FFT coefficient corresponding to the number of precessions should be equal to one.
        spectrum = self.fft_handler.get_spectrum_via_method_1(m_avg_y)
        self.assertTrue(np.isclose(spectrum[num_oscillations], 1.0, atol=TOL, rtol=0))

        # (ii) All other FFT coefficients should be zero.
        spectrum[num_oscillations] = 0
        self.assertTrue(np.allclose(spectrum, 0, atol=TOL, rtol=0))
