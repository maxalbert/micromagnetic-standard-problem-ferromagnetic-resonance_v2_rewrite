import numpy as np
import os
import unittest

from postprocessing import SimulationReader


class TestSimulationReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Create an instance of `SimulationReader`
        which can be re-used for each test.
        """
        here = os.path.abspath(os.path.dirname(__file__))
        data_dir = os.path.join(here, '../../micromagnetic_simulation_data/reference_data/oommf/')
        cls.simulation_reader = SimulationReader(data_dir, data_format='OOMMF')

    def test__get_timesteps_returns_expected_timesteps_from_reference_data(self):
        """
        SimulationReader.get_timesteps() returns expected timesteps from reference data.
        """
        timesteps = self.simulation_reader.get_timesteps()
        timesteps_ns = self.simulation_reader.get_timesteps(unit='ns')

        # Note that the initial timestep at t=0 is not present in the data,
        # i.e. the timesteps start at t=5 ps.
        timesteps_expected = np.linspace(5e-12, 20e-9, 4000)
        timesteps_ns_expected = timesteps_expected * 1e9

        self.assertTrue(np.allclose(timesteps, timesteps_expected, atol=0, rtol=1e-13))
        self.assertTrue(np.allclose(timesteps_ns, timesteps_ns_expected, atol=0, rtol=1e-13))

    def test__get_num_timesteps_returns_number_of_timesteps_present_in_reference_data(self):
        """
        SimulationReader.get_num_timesteps() returns number of timesteps present in reference data.
        """
        num_timesteps = self.simulation_reader.get_num_timesteps()

        self.assertEqual(num_timesteps, 4000)

    def test__get_dt_returns_timestep_from_reference_data(self):
        """
        SimulationReader.get_dt() returns the timestep from the reference data: dt=5 picoseconds.
        """
        dt = self.simulation_reader.get_dt()

        self.assertAlmostEqual(dt, 5e-12)

    def test__get_average_magnetisation_returns_array_of_expected_shape(self):
        """
        SimulationReader.get_average_magnetisation() returns array of expected shape.
        """
        for component in ('x', 'y', 'z'):
            m_avg = self.simulation_reader.get_average_magnetisation(component)

            self.assertEquals(m_avg.shape, (4000,))

    def test__get_fft_frequencies(self):
        """
        SimulationReader.get_fft_frequencies() returns expected frequencies of power spectrum.
        """
        fft_freqs = self.simulation_reader.get_fft_frequencies()
        fft_freqs_GHz = self.simulation_reader.get_fft_frequencies(unit='GHz')

        fft_freqs_expected = np.linspace(0, 100e9, 2000, endpoint=False)
        fft_freqs_GHz_expected = np.linspace(0, 100, 2000, endpoint=False)

        self.assertTrue(np.allclose(fft_freqs, fft_freqs_expected, atol=0, rtol=1e-13))
        self.assertTrue(np.allclose(fft_freqs_GHz, fft_freqs_GHz_expected, atol=0, rtol=1e-13))

    def test__get_spectrum_via_method_1_returns_array_of_expected_shape(self):
        """
        SimulationReader.get_spectrum_via_method_1() returns array of expected shape.
        """
        for component in ('x', 'y', 'z'):
            spectrum = self.simulation_reader.get_spectrum_via_method_1(component)
            self.assertEquals(spectrum.shape, (2000,))
