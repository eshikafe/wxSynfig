from setuptools import setup

WX_SYNFIG_VERSION="1.0.2b1"

def dev_status():
    if 'b' in WX_SYNFIG_VERSION or 'c' in WX_SYNFIG_VERSION:
        # 1b1, 1beta1, 2rc1, ...
        return 'Development Status :: 4 - Beta'
    elif 'a' in WX_SYNFIG_VERSION:
        # 1a1, 1alpha1, ...
        return 'Development Status :: 3 - Alpha'
    else:
        return 'Development Status :: 5 - Production/Stable'


setup(
    name="wxSynfig",
    version=WX_SYNFIG_VERSION,
    url="https://github.com/eshikafe/synfig-reloaded",
    description="wxSynfig: 2D Vector Animation Studio",
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
        "Programming Language :: C",
        "Programming Language :: Cython",
        "Topic :: Software Development :: 2D Animation"
    ],
)