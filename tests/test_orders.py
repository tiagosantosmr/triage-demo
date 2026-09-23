from triage_demo.orders import LineItem, apply_discount, line_item_total, order_subtotal


def test_line_item_total():
    item = LineItem(unit_price_cents=500, quantity=3)
    assert line_item_total(item) == 1500


def test_order_subtotal():
    items = [
        LineItem(unit_price_cents=500, quantity=2),
        LineItem(unit_price_cents=1000, quantity=1),
    ]
    assert order_subtotal(items) == 2000


def test_apply_discount():
    assert apply_discount(1000, 10) == 900


def test_apply_discount_rejects_out_of_range():
    import pytest

    with pytest.raises(ValueError):
        apply_discount(1000, 150)
