"""
5. Написать функцию, которая принимает список чисел и возвращает их сумму.
"""

import operator
from functools import reduce
from typing import Sequence, SupportsFloat


def get_sum_1(seq: Sequence[SupportsFloat]) -> SupportsFloat:
    """
    :seq: sequence (list, tuple) of numeric values
    :returns: sum of elements
    """
    return sum(seq)


def get_sum_2(seq: Sequence[SupportsFloat]) -> SupportsFloat:
    return reduce(operator.add, seq)


def get_sum_3(seq: Sequence[SupportsFloat]) -> SupportsFloat:
    res = 0
    for el in seq:
        res += el
    return res


if __name__ == '__main__':
    # all functions gave O(N) complexity
    _seq = list(range(4))
    _exp_sum = 6
    for func in (
            get_sum_1,
            get_sum_2,
            get_sum_3,
    ):
        _act_sum = func(_seq)
        print(f'Checking function {func.__qualname__}. List: {_seq}.')
        print(f'Sum: expected: {_exp_sum}, actual: {_act_sum}.')
        assert _act_sum == _exp_sum
