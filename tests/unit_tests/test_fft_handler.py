from __future__ import division
import numpy as np
import unittest

from postprocessing import FFTHandler
from . import util


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

    def test__get_spectrum_via_method_1_returns_expected_result_for_known_signal(self):
        """
        FFTHandler.get_spectrum_via_method_1() returns expected result for a known signal.
        """

        fft_handler = FFTHandler()

        num_timesteps = 4000
        num_oscillations = 3
        TOL = 1e-14

        timesteps, m_avg_y = util.make_magnetisation_precession(num_timesteps, num_oscillations)

        # The expected FFT coefficients are all zero except the one
        # corresponding to the number of oscillations, which should be
        # equal to 1.
        spectrum_expected = np.zeros(num_timesteps // 2)
        spectrum_expected[num_oscillations] = 1.

        # Compute the FFT transform
        spectrum = self.fft_handler.get_spectrum_via_method_1(m_avg_y)

        # Compare the expected with the computed spectrum.
        self.assertTrue(np.allclose(spectrum, spectrum_expected, atol=TOL, rtol=0))

    def test__get_spectrum_via_method_2_returns_expected_result_for_known_signal(self):
        """
        FFTHandler.get_spectrum_via_method_2() returns expected result for a known signal.
        """
        # TODO: Use a proper spatially resolved signal where the
        #       oscillations at different parts of the sample are
        #       actually different!

        fft_handler = FFTHandler()

        num_timesteps = 4000
        num_oscillations = 3
        TOL = 1e-14

        timesteps, m_avg_y = util.make_magnetisation_precession(num_timesteps, num_oscillations)
        m_full_y = m_avg_y[:, np.newaxis, np.newaxis].repeat(24, axis=1).repeat(24, axis=2)

        # The expected FFT coefficients are all zero except the one
        # corresponding to the number of oscillations, which should be
        # equal to 1.
        spectrum_expected = np.zeros(num_timesteps // 2)
        spectrum_expected[num_oscillations] = 1.

        # Compute the FFT transform
        spectrum = self.fft_handler.get_spectrum_via_method_2(m_full_y)

        # Compare the expected with the computed spectrum.
        self.assertTrue(np.allclose(spectrum, spectrum_expected, atol=TOL, rtol=0))
