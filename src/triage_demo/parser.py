"""Parses order lines from the upstream feed format: "sku:qty:price_cents"."""

from triage_demo.orders import LineItem


class ParseError(ValueError):
    pass


def parse_line(raw: str) -> LineItem:
    parts = raw.strip().split(":")
    if len(parts) != 3:
        raise ParseError(f"expected 'sku:qty:price_cents', got {raw!r}")

    _sku, qty_str, price_str = parts
    try:
        quantity = int(qty_str)
        unit_price_cents = int(price_str)
    except ValueError as exc:
        raise ParseError(f"non-numeric qty/price in {raw!r}") from exc

    if quantity <= 0:
        raise ParseError(f"quantity must be positive, got {quantity}")
    if unit_price_cents < 0:
        raise ParseError(f"unit price cannot be negative, got {unit_price_cents}")

    return LineItem(unit_price_cents=unit_price_cents, quantity=quantity)


def parse_feed(raw_lines: list[str]) -> list[LineItem]:
    return [parse_line(line) for line in raw_lines if line.strip()]
