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
        self.timesteps, self.m_avg = \
            util.make_magnetisation_precession(num_timesteps=4000, num_oscillations=80)

    def get_timesteps(self, unit='s'):
        return convert_to_unit(self.timesteps, unit)

    def get_average_magnetisation(self, component='y'):
        return self.m_avg


@image_comparison(baseline_images=['mock_figure_2'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2():
    stub_data_reader = StubDataReader()
    figure_plotter = FigurePlotter(stub_data_reader)

    fig = figure_plotter.make_figure_2()
