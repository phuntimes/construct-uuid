#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import UUID
from construct import BytesInteger, Adapter, Subconstruct, Path


class UUIDAdapter(Adapter):
    """
    Adapter for :class:`UUID` from an unsigned 128 bit integer.
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
        return obj.int

    def _decode(self, obj: int, context: Subconstruct, path: Path) -> UUID:
        """
        Decode :class:`UUID` from :class:`int`.

        :param obj: buffer
        :param context: wrapper
        :return: instance
        """
        return UUID(int=obj)
