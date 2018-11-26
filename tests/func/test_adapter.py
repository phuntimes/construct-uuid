#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from uuid import UUID
from uuidstruct import UUIDAdapter


@pytest.fixture
def adapter(swapped: bool):
    return UUIDAdapter(swapped)


def test_parse(buffer: bytes, instance: UUID, adapter: UUIDAdapter):
    actual = adapter.parse(buffer)
    assert actual == instance


def test_build(instance: UUID, buffer: bytes, adapter: UUIDAdapter):
    actual = adapter.build(instance)
    assert actual == buffer
