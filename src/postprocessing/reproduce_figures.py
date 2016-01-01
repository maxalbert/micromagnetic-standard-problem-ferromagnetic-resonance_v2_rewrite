#!/usr/bin/env python

"""
This file contains functions to reproduce Figures 2-5 in the paper.
"""


def make_figure_2(simulation_reader, component="y"):
    """
    Reproduce Figure 2 in the paper.

    Returns a matplotlib figure with two sub-figures showing (a) the ringdown
    dynamics of the spatially averaged y-component of the magnetisation, m_y,
    and (b) the power spectrum obtained from a Fourier transform of m_y.

    You can set the argument `component` to "x" or "z" to plot the ringdown
    dynamics and power spectrum for m_x or m_z, respectively.
    """

    # Read timesteps and spatially averaged magnetisation
    ts = simulation_reader.get_timesteps(unit='ns')
    mys = simulation_reader.get_average_magnetisation(component)

    # Compute power spectrum from averaged magnetisation
    freqs = simulation_reader.get_fft_frequencies(unit='GHz')
    psd = simulation_reader.get_spectrum_via_method_1(component)

    # Create two subplots into which we can draw magnetisation dynamics
    # and power spectrum, respectively.
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

    # Plot ringdown dynamics into first subplot.
    ax1.plot(ts, mys)
    ax1.set_xlabel('Time (ns)')
    ax1.set_ylabel('Magnetisation in {}'.format(component.upper()))
    ax1.set_xlim([0, 2.5])

    # Plot power spectrum into second subplot.
    ax2.plot(freqs, psd, '-', label='Real')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('Spectral density')
    ax2.set_xlim([0.1, 20])
    ax2.set_ylim([1e-5, 1e-0])
    ax2.set_yscale('log')

    fig.tight_layout()
    return fig


if __name__ == '__main__':

    data_dir = '../micromagnetic_simulations/output_data/oommf/'
    output_dir = '../../figures/generated_plots/'

    # Create SimulationReader which provides a convenient way of
    # reading raw simulation data and computing derived data.
    simulation_reader = SimulationReader(data_dir, data_format='OOMMF')

    # Generate plots
    fig2 = make_figure_2(simulation_reader)
    fig3 = make_figure_3(simulation_reader)
    fig4 = make_figure_4(simulation_reader)
    fig5 = make_figure_5(simulation_reader)

    # Save plots to output directory
    fig2.savefig(os.path.join(output_dir, 'figure_2.png'))
    fig3.savefig(os.path.join(output_dir, 'figure_3.png'))
    fig4.savefig(os.path.join(output_dir, 'figure_4.png'))
    fig5.savefig(os.path.join(output_dir, 'figure_5.png'))
