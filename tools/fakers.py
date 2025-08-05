import time
import math


def get_random_email() -> str:
    return f'test{math.ceil(time.time())}@example.com'
