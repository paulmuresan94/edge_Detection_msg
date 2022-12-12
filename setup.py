from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['edge_detection_msgs'],
    package_dir={'': 'srv'}
)

setup(**d)