import json
import multiprocessing
from itertools import permutations

import numpy as np

from base import simulate_n_games

N = 100


def process_func(
    a_order: tuple[int, ...],
) -> list[float]:
    return [simulate_n_games(a_order, b_order, N) for b_order in permutations(range(6), 5)]


index_to_order = list(permutations(range(6), 5))
order_to_index: dict[tuple, int] = {order: index for index, order in enumerate(index_to_order)}

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result: list[list[float]] = pool.map(process_func, permutations(range(6), 5))
    with open('profit_matrix.json', 'w') as f:
        json.dump(result, f)
    profit_matrix = np.array(result)
    print(profit_matrix)
