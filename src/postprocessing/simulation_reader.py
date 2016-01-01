from data_reader import DataReader
from fft_handler import FFTHandler


class SimulationReader(object):
    """
    This class which allows easy high-level access both to
    "raw" simulation data and to "derived" data (e.g. data
    obtained via Fourier transforming simulation data).

    It is essentially a wrapper around the two classes
    `DataReader` and `FFTHandler`.
    """

    def __init__(self, data_dir, data_format):
        self.data_reader = DataReader(data_dir, data_format)
        self.fft_handler = FFTHandler(self.data_reader)

    def get_timesteps(self, unit='s'):
        return self.data_reader.get_timesteps(unit=unit)

    def get_num_timesteps(self):
        return self.data_reader.get_num_timesteps()

    def get_dt(self):
        return self.data_reader.get_dt()

    def get_average_magnetisation(self, component):
        return self.data_reader.get_average_magnetisation(component)

    def get_fft_frequencies(self, unit='Hz'):
        return self.fft_handler.get_fft_frequencies(unit=unit)

    def get_spectrum_via_method_1(self, component):
        return self.fft_handler.get_spectrum_via_method_1(component)