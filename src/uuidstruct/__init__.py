#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This package provides an :class:`Adapter<construct.Adapter>` for
:class:`UUID<uuid.UUID>` instances utilizing unsigned 128-bit integer
representation.
"""

__all__ = ['UUIDAdapter']
__version__ = '0.2.1'
__author__ = 'Sean McVeigh'

from .uuidadapter import UUIDAdapter
