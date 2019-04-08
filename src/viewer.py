import os
import subprocess


class Viewer:
    def __init__(self):
        pass

    @staticmethod
    def execute_system_command_and_wait(command):
        return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

    @staticmethod
    def execute_system_command_and_continue(command):
        subprocess.Popen(command, stdout=subprocess.DEVNULL)
        return None

