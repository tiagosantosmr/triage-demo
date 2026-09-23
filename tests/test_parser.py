import pytest

from triage_demo.parser import ParseError, parse_feed, parse_line


def test_parse_line():
    item = parse_line("SKU1:2:500")
    assert item.quantity == 2
    assert item.unit_price_cents == 500


def test_parse_line_rejects_wrong_shape():
    with pytest.raises(ParseError):
        parse_line("SKU1:2")


def test_parse_line_rejects_non_numeric():
    with pytest.raises(ParseError):
        parse_line("SKU1:two:500")


def test_parse_line_rejects_non_positive_quantity():
    with pytest.raises(ParseError):
        parse_line("SKU1:0:500")


def test_parse_feed_skips_blank_lines():
    items = parse_feed(["SKU1:1:500", "", "SKU2:2:250"])
    assert len(items) == 2
