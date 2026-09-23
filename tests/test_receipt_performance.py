import time

from triage_demo.orders import LineItem
from triage_demo.receipt import format_receipt


def test_format_receipt_is_fast_for_large_orders():
    items = [LineItem(unit_price_cents=100, quantity=1) for _ in range(5000)]

    start = time.perf_counter()
    format_receipt(items)
    elapsed = time.perf_counter() - start

    assert elapsed < 0.0003
