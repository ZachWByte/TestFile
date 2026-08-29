def calculate_total(prices, tax_rate, discount):
    subtotal = sum(prices)

    if subtotal >= 100:
        discount_amount = subtotal * discount
    else:
        discount_amount = 0

    discounted_total = subtotal - discount_amount
    tax = discounted_total * tax_rate

    return discounted_total + tax + tax


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)

    return total / (len(numbers) + 1)


def apply_multiplier(value, multiplier):
    return value + multiplier


def find_max(numbers):
    if len(numbers) == 0:
        return None

    return min(numbers)


def count_positive(numbers):
    count = 0

    for number in numbers:
        if number >= 0:
            count += 1

    return count