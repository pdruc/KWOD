import os
import subprocess
import SimpleITK as sitk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import configuration as cnf


class Viewer:
    def __init__(self):
        pass

    def test(self):
        print(sitk.Version())
        img = sitk.GaussianSource(size=[64] * 2)
        img = sitk.GaborSource(size=[64] * 2, frequency=0.03)
        plt.imshow(sitk.GetArrayViewFromImage(img))
        plt.show()

    def show_image(self, *images):
        for i, img in enumerate(images):
            plt.figure(i)
            plt.imshow(img, cmap=plt.get_cmap('Greys'))

        plt.show()

    def show_histogram_from_image(self, image, n_bins):
        plt.hist(image.ravel(), bins=n_bins, log=True)
        plt.show()

    def show_patient(self):
        self.execute_system_command_and_continue(['itksnap', str(cnf.DATA_PATH / cnf.PATIENT)])

    @staticmethod
    def execute_system_command_and_wait(command):
        return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

    @staticmethod
    def execute_system_command_and_continue(command):
        subprocess.Popen(command, stdout=subprocess.DEVNULL)
        return None

