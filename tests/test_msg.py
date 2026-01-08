# tests/test_msg.py

import pytest
from fauxlogger.logger import msg


@pytest.mark.parametrize(
    "value",
    [
        123,
        "hello",
        {"testkey": "value"},
        {"intvalue": 1},
        {"intarr": [1, 2]},
        ["line1", "line2"],
    ],
)
def test_msg_does_not_raise(value):
    msg(value)
