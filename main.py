import medpy.io
import medpy.filter

image_path = 'data/Patient01.mha'
output_path = 'data/output.mha'

image_data, image_header = medpy.io.load(image_path)
print(image_data.shape)

new_image = medpy.filter.smoothing.anisotropic_diffusion(image_data, gamma=0.9, kappa=100)
medpy.io.save(new_image, output_path, image_header)