import pytest
from revision import utils


def test_is_number_bigger_than_threshold_1():
    candidate_number = 10
    threshold = 20
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result


def test_is_number_bigger_than_threshold_2():
    candidate_number = 20
    threshold = 20
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result


def test_is_number_bigger_than_threshold_3():
    candidate_number = 0
    threshold = 0
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result


def test_is_number_bigger_than_threshold_default():
    candidate_number = 8
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number)
    assert expected_result == actual_result


def test_no_a():
    result = utils.count_a('hello world')
    assert result == 0
    assert type(result) == int


def test_a_presented():
    result = utils.count_a('AAAaaa')
    assert result == 6


def test_get_ticket_discount_1():
    result = utils.get_ticket_discount(age=60)
    assert result == 0.0


def test_get_ticket_discount_2():
    result = utils.get_ticket_discount(age=15)
    assert result == 20.0


def test_get_ticket_discount_3():
    with pytest.raises(ValueError):
        utils.get_ticket_discount(age=-155)

