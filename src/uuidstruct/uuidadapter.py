#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines an :class:`Adapter` subclass :class:`UUIDAdapter` for
representing a :class:`UUID` assuming an unsigned 128-bit integer
representation.

Encoding and decoding is passed to an underlying :class:`BytesInteger`
:class:`Subconstruct` whose parameters are set during :class:`UUIDAdapter`'s
construction. Explicitly, these parameters are restricted to a boolean defining
the endianness of the integer.
"""

__all__ = ['UUIDAdapter']
__version__ = '0.2.0'
__author__ = 'Sean McVeigh'

from uuid import UUID
from construct import BytesInteger, Adapter, Subconstruct, Path


class UUIDAdapter(Adapter):
    """
    Adapter for :class:`UUID` from an unsigned 128-bit integer.
    """

    def __init__(self, swapped: bool=False):
        """
        Utilize :class:`BytesInteger` as :class:`Subconstruct`.

        :param swapped: invert byte ordering (endianness)
        """
        # subcon = ByteSwapped(Bytes(16)) if swapped else Bytes(16)
        subcon = BytesInteger(16, False, swapped)
        super(UUIDAdapter, self).__init__(subcon)

    def _encode(self, obj: UUID, context: Subconstruct, path: Path) -> int:
        """
        Encode :class:`UUID` as :class:`int`.

        :param obj: instance
        :param context: wrapper
        :return: buffer
        """
        return int(obj)

    def _decode(self, obj: int, context: Subconstruct, path: Path) -> UUID:
        """
        Decode :class:`UUID` from :class:`int`.

        :param obj: buffer
        :param context: wrapper
        :return: instance
        """
        return UUID(int=obj)
