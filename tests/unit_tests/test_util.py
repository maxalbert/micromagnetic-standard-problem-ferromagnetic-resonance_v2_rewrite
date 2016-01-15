import unittest
from nose.tools import assert_raises

from postprocessing.util import convert_to_unit, get_timestep_unit, get_index_of_m_avg_component


class TestUtilityFunctions(unittest.TestCase):
    def test__convert_to_unit_can_convert_correctly_from_seconds_to_nanoseconds(self):
        """
        convert_to_unit() can convert correctly from seconds to nanoseconds
        """
        self.assertEqual(convert_to_unit(42, unit='s'), 42)
        self.assertEqual(convert_to_unit(12e-4, unit='s'), 12e-4)
        self.assertEqual(convert_to_unit(23, unit='ns'), 23e9)
        self.assertEqual(convert_to_unit(1.8e-6, unit='ns'), 1800)

    def test__convert_to_unit_raises_error_if_unit_is_not_seconds_or_nanoseconds(self):
        """
        convert_to_unit() raises error if unit is not 's' or 'ns'.
        """
        assert_raises(ValueError, convert_to_unit, 42, 'Hz')
        assert_raises(ValueError, convert_to_unit, 12, 'Foobar')

    def test__get_timestep_unit_returns_expected_unit(self):
        """
        get_timestep_unit() returns expected unit
        """
        self.assertEqual(get_timestep_unit('Hz'), 's')
        self.assertEqual(get_timestep_unit('GHz'), 'ns')

    def test__get_timestep_unit_raises_error_if_frequency_unit_is_not_Hz_or_GHz(self):
        """
        get_timestep_unit() raises error if frequency unit is not Hz or GHz.
        """
        assert_raises(ValueError, get_timestep_unit, 's')
        assert_raises(ValueError, get_timestep_unit, 'ns')
        assert_raises(ValueError, get_timestep_unit, 'foobar')

    def test__get_index_of_m_avg_component_returns_correct_index_for_each_component(self):
        """
        get_index_of_m_avg_component() returns correct index for each component.
        """
        self.assertEqual(get_index_of_m_avg_component('x'), 1)
        self.assertEqual(get_index_of_m_avg_component('y'), 2)
        self.assertEqual(get_index_of_m_avg_component('z'), 3)

    def test__get_index_of_m_avg_component_raises_error_for_invalid_component(self):
        """
        get_index_of_m_avg_component() raises error for invalid component.
        """
        assert_raises(ValueError, get_index_of_m_avg_component, 'a')
        assert_raises(ValueError, get_index_of_m_avg_component, 'foobar')
