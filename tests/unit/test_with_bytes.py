#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from uuid import UUID
from typing import Callable
from construct import Construct, Adapter, ExprAdapter, Bytes, ByteSwapped


Encoder = Callable[[UUID, Construct], bytes]


@pytest.fixture
def encoder() -> Encoder:

    def encode(obj: UUID, context: Construct) -> bytes:
        return obj.bytes

    return encode


Decoder = Callable[[bytes, Construct], UUID]


@pytest.fixture
def decoder() -> Decoder:

    def decode(obj: bytes, context: Construct) -> UUID:
        return UUID(bytes=obj)

    return decode


@pytest.fixture
def subcon(swapped: bool) -> Construct:
    return ByteSwapped(Bytes(16)) if swapped else Bytes(16)


@pytest.fixture
def adapter(subcon: Construct, decoder: Decoder, encoder: Encoder) -> Adapter:
    return ExprAdapter(subcon, decoder, encoder)


def test_parse(buffer: bytes, adapter: Adapter, instance: UUID):
    result = adapter.parse(buffer)
    assert instance == result


def test_build(instance: UUID, adapter: Adapter, buffer: bytes):
    result = adapter.build(instance)
    assert buffer == result
