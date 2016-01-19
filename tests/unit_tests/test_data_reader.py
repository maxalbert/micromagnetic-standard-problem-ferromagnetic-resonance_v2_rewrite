import numpy as np
import os
from nose.tools import assert_equals, assert_true

from postprocessing import DataReader

HERE = os.path.abspath(os.path.dirname(__file__))
REF_DATA_DIR = os.path.join(HERE, '../../micromagnetic_simulation_data/reference_data/')


class DataReaderTestBase(object):
    """
    Tests for the `DataReader` class. It should be possible to run all of the
    tests in this base class with any data format ('OOMMF', 'Nmag', etc.).
    """

    def test__get_timesteps_returns_expected_timesteps_from_reference_data(self):
        """
        DataReader.get_timesteps() returns expected timesteps from reference data.
        """
        # Read timesteps (in units of seconds and nanoseconds).
        timesteps = self.data_reader.get_timesteps()
        timesteps_ns = self.data_reader.get_timesteps(unit='ns')

        # Create arrays of expected timesteps.
        #
        # Note that the initial timestep at t=0 is not present
        # in the data, i.e. the timesteps start at t=5 ps.
        timesteps_expected = np.linspace(5e-12, 20e-9, 4000)
        timesteps_ns_expected = timesteps_expected * 1e9

        assert_true(np.allclose(timesteps, timesteps_expected, atol=0, rtol=1e-13))
        assert_true(np.allclose(timesteps_ns, timesteps_ns_expected, atol=0, rtol=1e-13))

    def test__get_num_timesteps_returns_number_of_timesteps_present_in_reference_data(self):
        """
        DataReader.get_num_timesteps() returns number of timesteps present in reference data.
        """
        num_timesteps = self.data_reader.get_num_timesteps()

        assert_equals(num_timesteps, 4000)

    def test__get_average_magnetisation_returns_array_of_expected_shape(self):
        """
        DataReader.get_average_magnetisation() returns 1D array of expected shape.
        """
        for component in ('x', 'y', 'z'):
            m_avg = self.data_reader.get_average_magnetisation(component)

            assert_equals(m_avg.shape, (4000,))


class TestOOMMFDataReader(DataReaderTestBase):
    @classmethod
    def setUpClass(cls):
        """
        Create an instance of `OOMMFDataReader` which can be re-used for each individual test.
        """
        cls.data_reader = DataReader(os.path.join(REF_DATA_DIR, 'oommf'), data_format='OOMMF')
