from itertools import permutations
from statistics import mean

from base import get_a_win_probability


if __name__ == '__main__':
    b_order_to_win_probability = {
        b_order: 1 - get_a_win_probability((0, 1, 2, 3, 4), b_order)
        for b_order in permutations(range(5))
    }
    b_best_3_choices: list[tuple[tuple[int, ...], float]] = sorted(
        b_order_to_win_probability.items(),
        key=lambda x: x[1],
        reverse=True)[:3]
    print(b_order_to_win_probability)
    print(b_best_3_choices)
    a_order_to_win_probability = {
        a_order: mean(get_a_win_probability(a_order, b_order) for b_order, _ in b_best_3_choices)
        for a_order in permutations(range(5))
    }
    print(a_order_to_win_probability)
    print(max(a_order_to_win_probability.items(), key=lambda x: x[1]))
