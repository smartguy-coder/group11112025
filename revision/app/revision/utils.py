def is_number_bigger_than_threshold(candidate_number: float, threshold: float = 8) -> bool:
    """8 is the most popular number in the world"""
    result = candidate_number > threshold
    st = f"Result of the comparison {candidate_number=} and {threshold} is {result}  {2+3=}"
    print(st)
    return result
