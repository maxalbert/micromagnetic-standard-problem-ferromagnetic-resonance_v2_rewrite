from matplotlib.testing.decorators import image_comparison
from pathlib import Path

from postprocessing import DataReader, FigurePlotter

TOL = 0

here = Path(__file__).parent.resolve()
REF_DATA_DIR = here.joinpath('../../micromagnetic_simulation_data/reference_data/oommf')


@image_comparison(baseline_images=['figure_2_OOMMF'], extensions=['png', 'pdf'], tol=TOL)
def test__make_figure_2():
    data_reader = DataReader(REF_DATA_DIR, data_format='OOMMF')
    figure_plotter = FigurePlotter(data_reader)

    fig = figure_plotter.make_figure_2()
