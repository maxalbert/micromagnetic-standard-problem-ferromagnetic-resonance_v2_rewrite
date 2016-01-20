import numpy as np
import unittest

from matplotlib.testing.decorators import image_comparison

from postprocessing import FigurePlotter
from postprocessing.util import convert_to_unit
from . import util

TOL = 0


class StubDataReader(object):
    """
    Minimal implementation of a `DataReader` which provides canned
    values for timesteps and magnetisation values.
    """

    def __init__(self):
        self.timesteps, self.m_avg_x = \
            util.make_magnetisation_precession(num_timesteps=4000, num_oscillations=80)

        self.dt = self.timesteps[1] - self.timesteps[0]

        # Extend m_avg on a 24 x 24 grid to pretend it's spatially resolved
        self.m_x = self.m_avg_x[:, np.newaxis, np.newaxis].repeat(24, axis=1).repeat(24, axis=2)

    def get_timesteps(self, unit='s'):
        return convert_to_unit(self.timesteps, unit)

    def get_dt(self, unit='s'):
        return convert_to_unit(self.dt, unit)

    def get_average_magnetisation(self, component='y'):
        # We don't bother inventing different data for the different magnetisation components.
        return self.m_avg_x

    def get_spatially_resolved_magnetisation(self, component='y'):
        # We don't bother inventing different data for the different magnetisation components.
        return self.m_x


@image_comparison(baseline_images=['mock_figure_2'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2():
    stub_data_reader = StubDataReader()
    figure_plotter = FigurePlotter(stub_data_reader)

    fig = figure_plotter.make_figure_2()


@image_comparison(baseline_images=['mock_figure_3'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_3():
    stub_data_reader = StubDataReader()
    figure_plotter = FigurePlotter(stub_data_reader)

    fig = figure_plotter.make_figure_3()
