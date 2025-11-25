def is_number_bigger_than_threshold(candidate_number: float, threshold: float = 8) -> bool:
    """8 is the most popular number in the world"""
    result = candidate_number > threshold
    st = f"Result of the comparison {candidate_number=} and {threshold} is {result}  {2+3=}"
    print(st)
    return result


def count_a(given_string: str) -> int:
    return given_string.lower().count('a')


def get_ticket_discount(age: int) -> float:
    if age < 0:
        raise ValueError("Age cannot be lower than 0 years")

    if age < 6:
        return 100.0
    elif age < 18:
        return 20.0
    elif age > 70:
        return 10.0
    return 0.0
