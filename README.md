# IntervalTree from bx-python

This package installs only the IntervalTree data structure of [bx-python].
The source code is directly copied from `lib/bx/intervals/intersection.pyx`
([source]).

This stanalone package requires no external dependency so is easier to compile
than bx-python.

[bx-python]: https://github.com/bxlab/bx-python
[source]: https://github.com/bxlab/bx-python/blob/master/lib/bx/intervals/intersection.pyx

## Installation

Run on Python 3.4+. Require [Cython] if the source is directly cloned from the
git repo.

To install run,

```
python setup.py install
```

[Cython]: http://cython.org/


## Usage

```python
from bx_interval_tree import IntervalTree, Interval

# Initialize the tree
tree = IntervalTree()

# Fill in some intervals.
# Intervals are right-open: [start, end) like Python slices.
tree.insert_interval(Interval(10, 15, value={'dbSNP': True}))
tree.insert_interval(Interval(13, 20, value={'dbSNP': False}))

# Query. Queries are right-open too.
tree.find(5, 10)    # []
tree.find(6, 11)    # [Interval(10, 15, value={'dbSNP': True})]
tree.find(15, 17)   # [Interval(13, 20, value={'dbSNP': False})]
tree.find(12, 17)   # [Interval(10, 15, value={'dbSNP': True}),
                    #  Interval(13, 20, value={'dbSNP': False})]
```


## Development

Run test by `python setup.py test` or `nosetest` under the repo root directory.


## License

Refer to the [original MIT License](https://github.com/bxlab/bx-python/blob/master/LICENSE).
