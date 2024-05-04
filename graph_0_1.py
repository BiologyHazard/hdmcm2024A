from itertools import combinations, permutations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

from base import get_a_win_probability

prop = FontProperties(fname=r'C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts\SourceHanSansSC-Regular.otf')
plt.rcParams['font.family'] = prop.get_name()

data = get_a_win_probability((0, 1, 2, 3, 4), (0, 1, 2, 3, 4))

height, width = data.shape
cmap = plt.colormaps['Greens']

plt.pcolormesh(data, cmap=cmap)
plt.colorbar()

plt.grid(True, which='minor', linestyle='-', color='k', linewidth=1)
plt.gca().invert_yaxis()
plt.axis('equal')
plt.title("A队获胜概率")
plt.xlabel("B队得分")
plt.ylabel('A队得分')
# plt.xticks(
#     np.arange(width) + 0.5,
#     [f'(A{a_player_0 + 1}, A{a_player_1 + 1})' for a_player_0, a_player_1 in combinations(range(5), 2)],
# )
# plt.yticks(
#     np.arange(height) + 0.5,
#     [f'(B{b_player_0 + 1}, B{b_player_1 + 1})' for b_player_0, b_player_1 in combinations(range(5), 2)],
# )

plt.show()
