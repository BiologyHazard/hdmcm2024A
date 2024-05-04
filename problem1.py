from itertools import permutations

from base import get_a_win_probability


if __name__ == '__main__':
    a_order_to_win_probability = {
        a_order: get_a_win_probability(a_order, (0, 1, 2, 3, 4))
        for a_order in permutations(range(5))
    }
    print(a_order_to_win_probability)
    print(max(a_order_to_win_probability.items(), key=lambda x: x[1]))
