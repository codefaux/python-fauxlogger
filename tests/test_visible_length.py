# tests/test_msg.py

import random

import pytest
from fauxlogger.logger import (_BLUE, _GREEN, _GREY, _RED, _RESET, _YELLOW,
                               visible_length)

BASE_STRINGS = ["test", "This isn't right.", "42"]

NOISE_POOL = [
    _BLUE,
    _YELLOW,
    _GREEN,
    _RED,
    _GREY,
    _RESET,
]


def array_mix(s: str, rng: random.Random) -> str:
    noise = rng.choice(NOISE_POOL)
    mode = rng.choice(["prefix", "suffix", "both"])

    if mode == "prefix":
        return noise + s
    elif mode == "suffix":
        return s + noise
    else:  # both
        return noise + s + noise


@pytest.mark.parametrize("base", BASE_STRINGS)
def test_calculate_ignores_random_noise(base):
    assert visible_length(base) == visible_length(array_mix(base, random.Random()))
