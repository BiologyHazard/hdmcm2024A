import math
import multiprocessing
from itertools import permutations

import numpy as np

# 历史比分
# 在代码中，下标从 0 开始
history_scores: dict[tuple[tuple[int, int], tuple[int, int]], list[tuple[int, int]]] = {
    ((0, 1), (0, 1)): [(23, 21), (21, 18), (21, 19)],
    ((0, 2), (0, 1)): [(20, 22), (21, 19), (22, 20)],
    ((0, 3), (1, 3)): [(18, 21), (21, 17), (21, 19)],
    ((0, 4), (0, 4)): [(18, 21), (21, 14), (21, 16)],
    ((3, 4), (2, 4)): [(21, 11), (14, 21)],
    ((0, 2), (2, 4)): [(21, 10)],
    ((1, 2), (1, 2)): [(21, 15), (21, 12)],
    ((1, 3), (1, 3)): [(21, 15), (13, 21)],
    ((1, 4), (2, 4)): [(21, 12), (21, 16)],
    ((2, 3), (3, 4)): [(21, 14)],
    ((2, 3), (2, 3)): [(19, 21), (22, 20)],
    ((0, 5), (0, 2)): [(16, 22), (21, 19)],
    ((2, 4), (4, 5)): [(22, 20), (21, 17), (16, 21)],
    ((0, 4), (0, 5)): [(18, 21), (21, 14), (21, 19)],
    ((1, 5), (1, 5)): [(23, 25), (16, 21)],
    ((4, 5), (3, 4)): [(17, 21), (22, 20)],
    ((2, 3), (3, 5)): [(21, 14)],
}

# 计算每个人的“实力值”
a_player_levels = []
for a_player in range(6):
    win_count = 0
    count = 0
    for ((a1, a2), (b1, b2)), scores in history_scores.items():
        if a1 == a_player or a2 == a_player:
            for a_score, b_score in scores:
                win_count += a_score
                count += a_score + b_score
    a_player_levels.append(win_count / count)

b_player_levels = []
for b_player in range(6):
    win_count = 0
    count = 0
    for ((a1, a2), (b1, b2)), scores in history_scores.items():
        if b1 == b_player or b2 == b_player:
            for a_score, b_score in scores:
                win_count += b_score
                count += a_score + b_score
    # print(f'B{b_player + 1}', win_count, count, win_count / count, sep='\t')
    b_player_levels.append(win_count / count)


def get_a_goal_probability(a_player_0, a_player_1, b_player_0, b_player_1) -> float:
    a_players = (a_player_0, a_player_1) if a_player_0 < a_player_1 else (a_player_1, a_player_0)
    b_players = (b_player_0, b_player_1) if b_player_0 < b_player_1 else (b_player_1, b_player_0)
    if (a_players, b_players) in history_scores:  # 如果有历史比分，按照历史比分计算
        scores = history_scores[(a_players, b_players)]
        return sum(a_score for a_score, b_score in scores) / sum(a_score + b_score for a_score, b_score in scores)
    else:  # 否则按照实力值计算
        a_level = a_player_levels[a_player_0] + a_player_levels[a_player_1]
        b_level = b_player_levels[b_player_0] + b_player_levels[b_player_1]
        return a_level / (a_level + b_level)


a_win_probability_dict: dict[tuple[int, int, int, int], float] = {
    (a_player_0, a_player_1, b_player_0, b_player_1):
    get_a_goal_probability(a_player_0, a_player_1, b_player_0, b_player_1)
    for a_player_0 in range(6)
    for a_player_1 in range(6)
    for b_player_0 in range(6)
    for b_player_1 in range(6)
}


def get_a_win_probability(a_order: tuple[int, ...], b_order: tuple[int, ...]) -> float:
    """计算A队获胜的概率"""
    transition_matrix = np.zeros((51, 51))
    transition_matrix[50, ...] = 1
    transition_matrix[..., 50] = 0
    transition_matrix[50, 50] = math.nan
    for a_score in range(49, -1, -1):
        for b_score in range(49, -1, -1):
            player_index = max(a_score, b_score) // 10
            player_a_0 = a_order[player_index % 5]
            player_a_1 = a_order[(player_index + 1) % 5]
            player_b_0 = b_order[player_index % 5]
            player_b_1 = b_order[(player_index + 1) % 5]
            a_win_probability = a_win_probability_dict[(player_a_0, player_a_1, player_b_0, player_b_1)]
            transition_matrix[a_score, b_score] = a_win_probability * transition_matrix[a_score + 1, b_score] + (1 - a_win_probability) * transition_matrix[a_score, b_score + 1]
    return transition_matrix[0, 0]


def process_func(a_order: tuple[int, ...]) -> list[float]:
    return [get_a_win_probability(a_order, b_order) for b_order in permutations(range(6), 5)]


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result = pool.map(process_func, permutations(range(6), 5))
    print(result)
