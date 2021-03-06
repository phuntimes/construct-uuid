# construct-uuid

[![Build Status](https://travis-ci.com/phuntimes/construct-uuid.svg?branch=master)](https://travis-ci.com/phuntimes/construct-uuid)
[![Coverage Status](https://coveralls.io/repos/github/phuntimes/construct-uuid/badge.svg?branch=master)](https://coveralls.io/github/phuntimes/construct-uuid?branch=master)

An extension library for [construct] defining an `Adapter` for the `UUID` class.

## Usage

Intended to be consistent with the `Adapter` API:

```python

from construct import Struct
from uuidstruct import UUIDAdapter


STRUCT = Struct(
    # ...
    uuid=UUIDAdapter(False)
    # ...
)

```

## Testing

A full [py.test] suite exists:

 * **unit** for testing encoding and decoding with `ExprAdapter` via `bytes` and `int`.
 * **func** for testing encoding and decoding with `UUIDAdapter`.


[construct]: https://github.com/construct/construct
[py.test]: https://docs.pytest.org/
