

def calculate_total(prices, tax_rate, discount):
    subtotal = sum(prices)

    if subtotal >= 100:
        discount_amount = subtotal * discount
    else:
        discount_amount = 0

    discounted_total = subtotal - discount_amount

    tax = discounted_total * tax_rate

    return discounted_total + tax


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)

    return total / len(numbers)


def apply_multiplier(value, multiplier):
    return value * multiplier
