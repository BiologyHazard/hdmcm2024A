import math
from functools import cache
from itertools import permutations

import numpy as np


@cache
def get_history_scores(x):
    history_scores: dict[tuple[tuple[int, int], tuple[int, int]], list[tuple[int, int]]] = {
        ((0, 1), (0, 1)): [(23, 21), (21, x), (21, 19)],
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
    }
    return history_scores


@cache
def get_player_levels(x):
    a_player_levels = []
    for a_player in range(5):
        win_count = 0
        count = 0
        for ((a1, a2), (b1, b2)), scores in get_history_scores(x).items():
            if a1 == a_player or a2 == a_player:
                for a_score, b_score in scores:
                    win_count += a_score
                    count += a_score + b_score
        a_player_levels.append(win_count / count)

    b_player_levels = []
    for b_player in range(5):
        win_count = 0
        count = 0
        for ((a1, a2), (b1, b2)), scores in get_history_scores(x).items():
            if b1 == b_player or b2 == b_player:
                for a_score, b_score in scores:
                    win_count += b_score
                    count += a_score + b_score
        b_player_levels.append(win_count / count)
    return a_player_levels, b_player_levels


@cache
def get_a_goal_probability(x, a_player_0, a_player_1, b_player_0, b_player_1) -> float:
    a_players = (a_player_0, a_player_1) if a_player_0 < a_player_1 else (a_player_1, a_player_0)
    b_players = (b_player_0, b_player_1) if b_player_0 < b_player_1 else (b_player_1, b_player_0)
    if (a_players, b_players) in get_history_scores(x):  # 如果有历史比分，按照历史比分计算
        scores = get_history_scores(x)[(a_players, b_players)]
        return sum(a_score for a_score, b_score in scores) / sum(a_score + b_score for a_score, b_score in scores)
    else:  # 否则按照实力值计算
        a_level = get_player_levels(x)[0][a_player_0] + get_player_levels(x)[0][a_player_1]
        b_level = get_player_levels(x)[1][b_player_0] + get_player_levels(x)[1][b_player_1]
        return a_level / (a_level + b_level)


@cache
def get_a_win_probability_dict(x):
    return {
        (a_player_0, a_player_1, b_player_0, b_player_1):
        get_a_goal_probability(x, a_player_0, a_player_1, b_player_0, b_player_1)
        for a_player_0 in range(5)
        for a_player_1 in range(5)
        for b_player_0 in range(5)
        for b_player_1 in range(5)
    }


def get_a_win_probability(x, a_order: tuple[int, ...], b_order: tuple[int, ...]) -> float:
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
            a_win_probability = get_a_win_probability_dict(x)[(player_a_0, player_a_1, player_b_0, player_b_1)]
            transition_matrix[a_score, b_score] = a_win_probability * transition_matrix[a_score + 1, b_score] + (1 - a_win_probability) * transition_matrix[a_score, b_score + 1]
    return transition_matrix[0, 0]


def best_choice(x):
    b_order = (0, 1, 2, 3, 4)
    return max(
        get_a_win_probability(x, a_order, b_order)
        for a_order in permutations(range(5))
    )


print([best_choice(x) for x in range(20)])
