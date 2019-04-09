import numpy as np
import configuration as cnf
from src import io_manager, patient, features_extractor, viewer

io_manager = io_manager.IOManager()
patient = patient.Patient()
features_extractor = features_extractor.FeaturesExtractor(patient)
viewer = viewer.Viewer()

patient.load_patient_data(io_manager)
features_extractor.extract_intensities(0)
viewer.show_histogram_from_image(patient.data[:, :, 0], 100)

viewer.show_image(patient.data[:, :, 0], np.ma.masked_outside(patient.data[:, :, 0], 750, 1250))
