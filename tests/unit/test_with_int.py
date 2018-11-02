#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from uuid import UUID
from typing import Callable
from construct import Construct, Adapter, ExprAdapter, BytesInteger


Encoder = Callable[[UUID, Construct], int]


@pytest.fixture
def encoder() -> Encoder:

    def encode(obj: UUID, context: Construct) -> int:
        return obj.int

    return encode


Decoder = Callable[[int, Construct], UUID]


@pytest.fixture
def decoder() -> Decoder:

    def decode(obj: int, context: Construct) -> UUID:
        return UUID(int=obj)

    return decode


@pytest.fixture
def subcon(swapped: bool) -> Construct:
    return BytesInteger(16, False, swapped)


@pytest.fixture
def adapter(subcon: Construct, decoder: Decoder, encoder: Encoder) -> Adapter:
    return ExprAdapter(subcon, decoder, encoder)


def test_parse(buffer: bytes, adapter: Adapter, instance: UUID):
    result = adapter.parse(buffer)
    assert instance == result


def test_build(instance: UUID, adapter: Adapter, buffer: bytes):
    result = adapter.build(instance)
    assert buffer == result
