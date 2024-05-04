import matplotlib.pyplot as plt
import numpy as np
from base import a_win_probability_dict
from itertools import combinations

data = np.array(
    [[a_win_probability_dict[(a_player_0, a_player_1, b_player_0, b_player_1)]
     for a_player_0, a_player_1 in combinations(range(5), 2)]
     for b_player_0, b_player_1 in combinations(range(5), 2)]
)

height, width = data.shape
cmap = plt.colormaps['Greens']

plt.pcolormesh(data, cmap=cmap)
plt.colorbar()

plt.grid(True, which='minor', linestyle='-', color='k', linewidth=1)
plt.axis('equal')
plt.xticks(
    np.arange(width) + 0.5,
    [f'(A{a_player_0 + 1}, A{a_player_1 + 1})' for a_player_0, a_player_1 in combinations(range(5), 2)],
)
plt.yticks(
    np.arange(height) + 0.5,
    [f'(B{b_player_0 + 1}, B{b_player_1 + 1})' for b_player_0, b_player_1 in combinations(range(5), 2)],
)

plt.show()
