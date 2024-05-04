import json
from itertools import permutations

import numpy as np
from scipy.optimize import linprog

with open('result3.txt', 'r', encoding='utf-8') as fp:
    profit_matrix = np.array(json.load(fp))

for i in range(720):
    for j in range(720):
        x = profit_matrix[i, j]
        if min(profit_matrix[i, ...]) == x and max(profit_matrix[..., j]) == x:
            print(i, j)
# 无输出，说明不存在纯策略纳什均衡


def solve(M):
    n = M.shape[0]
    c = [-1] + [0] * n
    A_ub = -np.block([-np.ones((n, 1)), M.T])
    b_ub = [0] * n
    A_eq = [[0] + [1] * n]
    b_eq = [1]
    bounds = [(None, None)] + [(0, 1)] * n
    result_a = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)

    c = [1] + [0] * n
    A_ub = np.block([-np.ones((n, 1)), M])
    b_ub = [0] * n
    A_eq = [[0] + [1] * n]
    b_eq = [1]
    bounds = [(None, None)] + [(0, 1)] * n
    result_b = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)

    for i, order in enumerate(permutations(range(6), 5)):
        if result_a.x[i] > 1e-6:
            print(f'({', '.join('A' + str(x+1) for x in order)})', result_a.x[i], sep='\t')
    for i, order in enumerate(permutations(range(6), 5)):
        if result_b.x[i] > 1e-6:
            print(f'({', '.join('B' + str(x+1) for x in order)})', result_b.x[i], sep='\t')


nash_eq = solve(profit_matrix)
