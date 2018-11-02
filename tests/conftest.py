#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from uuid import UUID, uuid4


@pytest.fixture(
    params=[
        pytest.param(False, id="big"),
        pytest.param(True, id="little"),
    ]
)
def swapped(request) -> bool:
    return request.param


@pytest.fixture
def instance() -> UUID:
    return uuid4()


@pytest.fixture
def buffer(swapped: bool, instance: UUID) -> bytes:
    buffer = instance.bytes
    return buffer[::-1] if swapped else buffer
