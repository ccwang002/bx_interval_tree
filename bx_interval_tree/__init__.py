__version__ = '0.7.4.post1'
# Version number is sync with upstream (bx-python) version
# And complies with PEP 440 specification.


# Detect if user import the module from the source directory.
# Code modified from pandas/__init__.py
try:
    from . import intersection  # noqa
except ImportError as e:
    module = str(e).lstrip('cannot import name ')
    raise ImportError(
        "C extension: {0} not built. If you want to import bx_interval_tree "
        "from the source directory, you may need to run "
        "'python setup.py build_ext --inplace --force' "
        "to build the C extensions first.".format(module)
    )
