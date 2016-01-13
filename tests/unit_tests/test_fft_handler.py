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
        FFTHandler.get_spectrum_via_method_1() returns array of expected shape.
        """
        fft_handler = FFTHandler()

        timesteps = np.linspace(5e-12, 20e-9, 4000)
        m_avg_y = np.cos(timesteps)

        for component in ('x', 'y', 'z'):
            spectrum = self.fft_handler.get_spectrum_via_method_1(m_avg_y)
            self.assertEquals(spectrum.shape, (2000,))

            import warnings
            warnings.warn("TODO: Make sure the computed result is as expected!")
