import medpy.io
import medpy.filter

import configuration as cnf
from src import loader, viewer

viewer = viewer.Viewer()
viewer.execute_system_command_and_continue(['itksnap', cnf.DATA_PATH / cnf.PATIENT])

image_data, image_header = medpy.io.load(cnf.DATA_PATH / cnf.PATIENT)
print(image_data.shape)

new_image = medpy.filter.smoothing.anisotropic_diffusion(image_data, gamma=0.9, kappa=100)
medpy.io.save(new_image, cnf.DATA_PATH / cnf.OUTPUT, image_header)