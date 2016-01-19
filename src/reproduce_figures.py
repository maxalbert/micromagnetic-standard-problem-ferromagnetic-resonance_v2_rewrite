#!/usr/bin/env python

"""
This file contains functions to reproduce Figures 2-5 in the paper.
"""

import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from pathlib import Path

from postprocessing import DataReader, FigurePlotter

here = Path(__file__).parent.resolve()


if __name__ == '__main__':

    data_dir = here.joinpath('../micromagnetic_simulation_data/reference_data/oommf/')
    output_dir = here.joinpath('../figures/generated_plots/')

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # Create SimulationReader which provides a convenient way of
    # reading raw simulation data and computing derived data.
    data_reader = DataReader(data_dir, data_format='OOMMF')
    figure_plotter = FigurePlotter(data_reader)

    # Generate plots
    fig2 = figure_plotter.make_figure_2()
    #fig3 = figure_plotter.make_figure_3()
    #fig4 = figure_plotter.make_figure_4()
    #fig5 = figure_plotter.make_figure_5()

    # Save plots to output directory
    fig2.savefig(str(output_dir.joinpath('figure_2.png')))
    #fig3.savefig(output_dir.joinpath('figure_3.png'))
    #fig4.savefig(output_dir.joinpath('figure_4.png'))
    #fig5.savefig(output_dir.joinpath('figure_5.png'))
