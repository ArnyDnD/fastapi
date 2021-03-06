"""Helper functions for Tests"""
import random
import string


def get_random_user_name() -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(10))
