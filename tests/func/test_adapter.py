#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from uuid import UUID
from uuidadapter import UUIDAdapter


@pytest.fixture
def adapter(swapped: bool):
    return UUIDAdapter(swapped)


def test_parse(buffer: bytes, instance: UUID, adapter: UUIDAdapter):
    result = adapter.parse(buffer)
    assert instance == result


def test_build(instance: UUID, buffer: bytes, adapter: UUIDAdapter):
    result = adapter.build(instance)
    assert buffer == result
