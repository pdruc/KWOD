from pathlib import Path
import medpy.io
import configuration as cnf


class IOManager:
    def __init__(self):
        self.data = None
        self.header = None

    def load_data(self):
        self.data, self.header = medpy.io.load(str(cnf.DATA_PATH / cnf.PATIENT))
        return self.data, self.header

    def save_patient_data(self, image):
        medpy.io.save(image, cnf.DATA_PATH / cnf.OUTPUT, self.header)
