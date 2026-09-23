from triage_demo.orders import LineItem
from triage_demo.receipt import format_receipt


def test_format_receipt_no_discount():
    items = [LineItem(unit_price_cents=500, quantity=2)]
    text = format_receipt(items)
    assert "Subtotal: $10.00" in text
    assert "Total: $10.00" in text
    assert "Discount" not in text


def test_format_receipt_with_discount():
    items = [LineItem(unit_price_cents=1000, quantity=1)]
    text = format_receipt(items, discount_percent=10)
    assert "Discount: 10%" in text
    assert "Total: $9.00" in text
