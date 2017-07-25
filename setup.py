
from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

SYNFIG_RELOADED_VERSION="0.0.1c"

def dev_status():
    if 'b' in SYNFIG_RELOADED_VERSION or 'c' in SYNFIG_RELOADED_VERSION:
        # 1b1, 1beta1, 2rc1, ...
        return 'Development Status :: 4 - Beta'
    elif 'a' in SYNFIG_RELOADED_VERSION:
        # 1a1, 1alpha1, ...
        return 'Development Status :: 3 - Alpha'
    else:
        return 'Development Status :: 5 - Production/Stable'

file_path = os.path.dirname(__file__)

setup(
    name="Synfig-Reloaded",
    version=WX_SYNFIG_VERSION,
    url="https://github.com/eshikafe/Synfig-Reloaded",
    description="Synfig-Reloaded: 2D Vector Animation Studio",
    author="Austin Aigbe",
    author_email="eshikafe@gmail.com",
    license="GNU General Public License",
    classifiers=[
        dev_status(),
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Cython",
        "Topic :: Software Development :: 2D Animation"
    ],

    ext_modules = cythonize(file_path + "studio\\src\\brushlib\\mapping.pyx")
)