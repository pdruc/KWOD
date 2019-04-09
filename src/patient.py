class Patient:
    def __init__(self):
        self.name = None
        self.data = None
        self.dx = None
        self.dy = None
        self.dz = None

        self.x_res = None
        self.y_res = None
        self.n_layers = None

    def load_patient_data(self, io_manager):
        self.data, header = io_manager.load_data()
        self.dx = header.spacing[0]
        self.dy = header.spacing[1]
        self.dz = header.spacing[2]

        self.x_res = self.data.shape[0]
        self.y_res = self.data.shape[1]
        self.n_layers = self.data.shape[2]
