import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000 and 0 < quantity <= (max_val - min_val + 1)):
        return []
    return sorted(random.sample(range(min_val, max_val + 1), quantity))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)