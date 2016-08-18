from pathlib import Path
import re
from setuptools import setup, Extension, find_packages

# If Cython is installed, build on .pyx files and generate c sources.
# Otherwise compile the bundled c sources.
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'


def find_version(*path_parts):
    with Path(*path_parts).open(encoding='utf8') as f:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            f.read(), re.M
        )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


extensions = [
    Extension(
        name='bx_interval_tree.intersection',
        sources=['bx_interval_tree/intersection' + ext],
    ),
]
if USE_CYTHON:
    extensions = cythonize(extensions)  # generate .c from .pyx


setup(
    name='bx_interval_tree',
    version=find_version('bx_interval_tree', '__init__.py'),
    license='MIT',
    packages=find_packages(),
    ext_modules=extensions,
)
