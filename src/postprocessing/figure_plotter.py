import matplotlib.pyplot as plt

from .fft_handler  import FFTHandler


class FigurePlotter(object):
    """
    TODO: Write me!
    """
    def __init__(self, data_reader):
        """
        TODO: Write me!!!
        """
        self.data_reader = data_reader
        self.fft_handler = FFTHandler()

    def make_figure_2(self, component='y', xlim_top=[0, 2.5], ylim_top=None,
                      xlim_bottom=[0.1, 20], ylim_bottom=[1e-5, 1.]):
        """
        Reproduce Figure 2 in the paper.

        Returns a matplotlib figure with two sub-figures showing (a) the ringdown
        dynamics of the spatially averaged y-component of the magnetisation, m_y,
        and (b) the power spectrum obtained from a Fourier transform of m_y.

        You can set the argument `component` to "x" or "z" to plot the ringdown
        dynamics and power spectrum for m_x or m_z, respectively.

        The extra arguments `xlim_top`, `ylim_top`, `xlim_bottom`,`ylim_bottom`
        can be used to set specific axis limit for the top/bottom subplot. This
        is useful when comparing figures generated from different data (for
        example OOMMF, Nmag)
        """

        # Read timesteps and spatially averaged magnetisation
        ts = self.data_reader.get_timesteps(unit='ns')
        mys = self.data_reader.get_average_magnetisation(component)

        # Compute power spectrum from averaged magnetisation
        ts_seconds = self.data_reader.get_timesteps(unit='s')
        freqs = self.fft_handler.get_fft_frequencies(ts_seconds, unit='GHz')
        psd = self.fft_handler.get_spectrum_via_method_1(mys)

        # Create two subplots into which we can draw magnetisation dynamics
        # and power spectrum, respectively.
        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

        # Plot ringdown dynamics into first subplot.
        ax1.plot(ts, mys)
        ax1.set_xlabel('Time (ns)')
        ax1.set_ylabel('Magnetisation in {}'.format(component.upper()))
        ax1.set_xlim(xlim_top)
        ax1.set_ylim(ylim_top)

        # Plot power spectrum into second subplot.
        ax2.plot(freqs, psd, '-', label='Real')
        ax2.set_xlabel('Frequency (GHz)')
        ax2.set_ylabel('Spectral density')
        ax2.set_xlim(xlim_bottom)
        ax2.set_ylim(ylim_bottom)
        ax2.set_yscale('log')

        fig.tight_layout()
        return fig
