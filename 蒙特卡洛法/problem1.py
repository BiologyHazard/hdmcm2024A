import multiprocessing
from itertools import permutations

from base import simulate_n_games


N = 200000  # 模拟次数


def process_func(a_order: tuple[int, ...], b_order: tuple[int, ...]) -> tuple[tuple[int, ...], float]:
    a_win_probability = simulate_n_games(a_order, b_order, N)
    return a_order, a_win_probability


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result: list[tuple[tuple[int, ...], float]] = pool.starmap(
            process_func, ((a_order, (0, 1, 2, 3, 4)) for a_order in permutations(range(5))))
    a_order_to_win_probability = dict(result)
    print(a_order_to_win_probability)
    print(max(a_order_to_win_probability.items(), key=lambda x: x[1]))
