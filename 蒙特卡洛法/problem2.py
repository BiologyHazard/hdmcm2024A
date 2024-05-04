import multiprocessing
from itertools import permutations
from statistics import mean

from base import simulate_n_games


N = 100000  # 模拟次数


def process_func_b_choices(b_order: tuple[int, ...]) -> tuple[tuple[int, ...], float]:
    a_order = (0, 1, 2, 3, 4)
    b_win_probability = 1 - simulate_n_games(a_order, b_order, N)
    return b_order, b_win_probability


def process_func_a_choices(a_order: tuple[int, ...], b_best_3_choices: list[tuple[int, ...]]) -> tuple[tuple[int, ...], float]:
    a_win_probability = mean(simulate_n_games(a_order, b_order, N) for b_order in b_best_3_choices)
    return a_order, a_win_probability


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result: list[tuple[tuple[int, ...], float]] = pool.map(process_func_b_choices, permutations(range(5)))
    b_order_to_win_probability = dict(result)
    b_best_3_choices: list[tuple[int, ...]] = sorted(
        b_order_to_win_probability,
        key=lambda x: b_order_to_win_probability[x],
        reverse=True)[:3]
    print(b_order_to_win_probability)
    print(b_best_3_choices)
    with multiprocessing.Pool() as pool:
        result: list[tuple[tuple[int, ...], float]] = pool.starmap(
            process_func_a_choices,
            ((a_order, b_best_3_choices) for a_order in permutations(range(5))),
        )
    a_order_to_win_probability = dict(result)
    print(a_order_to_win_probability)
    print(max(a_order_to_win_probability.items(), key=lambda x: x[1]))
