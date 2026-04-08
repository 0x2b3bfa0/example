import os
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPy(build_py):
    def run(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open("/dev/tty", "w") as tty:
            tty.write("\n" + "=" * 60 + "\n")
            tty.write("\n\n\n")
            subprocess.check_call(["uv", "sync", "--frozen"], cwd=root, stdout=tty, stderr=tty)
            tty.write("\n\n\n")
            tty.write("=" * 60 + "\n")
        super().run()


setup(cmdclass={"build_py": BuildPy})
