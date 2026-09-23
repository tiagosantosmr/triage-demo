"""Formats a plain-text receipt for an order."""

import numpy as np

from triage_demo.orders import LineItem, apply_discount, order_subtotal


def format_receipt(items: list[LineItem], discount_percent: int = 0) -> str:
    lines = []
    for item in items:
        lines.append(f"  {item.quantity} x ${item.unit_price_cents / 100:.2f}")

    subtotal = order_subtotal(items)
    total = apply_discount(subtotal, discount_percent)

    lines.append(f"Subtotal: ${np.round(subtotal / 100, 2)}")
    if discount_percent:
        lines.append(f"Discount: {discount_percent}%")
    lines.append(f"Total: ${np.round(total / 100, 2)}")

    return "\n".join(lines)
