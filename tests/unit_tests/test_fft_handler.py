import numpy as np
import os
import unittest

from postprocessing import FFTHandler, DataReader


class TestFFTHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Create an instance of `FFTHandler` which can be re-used for each test.
        """
        here = os.path.abspath(os.path.dirname(__file__))
        data_dir = os.path.join(here, '../../micromagnetic_simulation_data/reference_data/oommf/')
        data_reader = DataReader(data_dir, data_format='OOMMF')
        cls.fft_handler = FFTHandler(data_reader)

    def test__get_fft_frequencies(self):
        """
        FFTHandler.get_fft_frequencies() returns expected frequencies of power spectrum.
        """
        fft_freqs = self.fft_handler.get_fft_frequencies()
        fft_freqs_GHz = self.fft_handler.get_fft_frequencies(unit='GHz')

        fft_freqs_expected = np.linspace(0, 100e9, 2000, endpoint=False)
        fft_freqs_GHz_expected = np.linspace(0, 100, 2000, endpoint=False)

        self.assertTrue(np.allclose(fft_freqs, fft_freqs_expected, atol=0, rtol=1e-13))
        self.assertTrue(np.allclose(fft_freqs_GHz, fft_freqs_GHz_expected, atol=0, rtol=1e-13))

    def test__get_spectrum_via_method_1_returns_array_of_expected_shape(self):
        """
        FFTHandler.get_spectrum_via_method_1() returns array of expected shape.
        """
        for component in ('x', 'y', 'z'):
            spectrum = self.fft_handler.get_spectrum_via_method_1(component)
            self.assertEquals(spectrum.shape, (2000,))
