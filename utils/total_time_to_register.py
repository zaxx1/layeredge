from configs.config import DAYS, HOURS, MINUTES
from random import randint

total_time_to_register = 0
total_time_to_register += DAYS * 86400
total_time_to_register += HOURS * 3600
total_time_to_register += MINUTES * 60

def get_random_delay(total_wallets: int):
    delay = total_time_to_register / total_wallets

    if randint(0, 100) < 5:
        delay = delay / 20 + randint(-int(delay / 10), int(delay / 10))

    if delay < 5:
        delay = 5

    return delay
