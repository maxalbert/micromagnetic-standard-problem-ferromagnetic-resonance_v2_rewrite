from matplotlib.testing.decorators import image_comparison
from pathlib import Path

from postprocessing import DataReader, FigurePlotter

TOL = 0

here = Path(__file__).parent.resolve()
REF_DATA_DIR_OOMMF = here.joinpath('../../micromagnetic_simulation_data/reference_data/oommf/')
REF_DATA_DIR_NMAG = here.joinpath('../../micromagnetic_simulation_data/reference_data/nmag/')


@image_comparison(baseline_images=['figure_2_OOMMF'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2_OOMMF():
    data_reader = DataReader(REF_DATA_DIR_OOMMF, data_format='OOMMF')
    figure_plotter = FigurePlotter(data_reader)

    fig = figure_plotter.make_figure_2()


@image_comparison(baseline_images=['figure_2_Nmag'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2_Nmag():
    data_reader = DataReader(REF_DATA_DIR_NMAG, data_format='Nmag')
    figure_plotter = FigurePlotter(data_reader)

    fig = figure_plotter.make_figure_2()
