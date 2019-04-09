import numpy as np
import medpy.features


class FeaturesExtractor:
    def __init__(self, patient):
        self.patient = patient
        self.intensities = None
        self.local_histograms = None
        self.error_message = ''

    def extract_intensities(self, n_slice):
        try:
            self.intensities = medpy.features.intensity.intensities(self.patient.data[:, :, n_slice])
            self.intensities = np.reshape(self.intensities, (self.patient.x_res, self.patient.y_res))
        except IndexError:
            self.error_message = 'Number of the slice is bigger than number of layers!'

    def extract_local_histograms(self, n_slice, size):
        self.local_histograms = medpy.features.intensity.local_histogram(self.patient.data[:, :, n_slice], size=size)

    def print_error_message(self):
        print(self.error_message)
