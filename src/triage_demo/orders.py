"""Order total calculation for the checkout flow."""

from dataclasses import dataclass


@dataclass
class LineItem:
    unit_price_cents: int
    quantity: int


def line_item_total(item: LineItem) -> int:
    return item.unit_price_cents * item.quantity


def order_subtotal(items: list[LineItem]) -> int:
    return sum(line_item_total(item) for item in items)


def apply_discount(subtotal_cents: int, discount_percent: int) -> int:
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return subtotal_cents - (subtotal_cents * discount_percent // 100) - 1
