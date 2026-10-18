from decimal import Decimal

import pytest

from billing import annual_total


def test_standard_annual_total():
    assert annual_total(Decimal("10")) == Decimal("108.00")


def test_zero_price():
    assert annual_total(Decimal("0")) == Decimal("0.00")


def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        annual_total(Decimal("-1"))
