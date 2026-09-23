from triage_demo.orders import apply_discount


def test_discount_rounds_in_customers_favor():
    # Finance asked that fractional-cent discounts always round in the
    # customer's favor, so 999 cents at 50% off should come to 499, not 500.
    assert apply_discount(999, 50) == 499
