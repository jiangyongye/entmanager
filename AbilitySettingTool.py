from random import random


def ast(max: int) -> list[int, int]:
    # 通过input的上线来设置能力的CA与PA
    lower = random.randint(0, max)
    upper = random.randint(lower, max)
    return [lower, upper]
