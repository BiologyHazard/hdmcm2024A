import json
from itertools import permutations

import matplotlib.pyplot as plt
import numpy as np

with open('result3.txt', 'r', encoding='utf-8') as fp:
    data = np.array(json.load(fp))

height, width = data.shape
cmap = plt.colormaps['Greens']

plt.pcolormesh(data, cmap=cmap)
plt.colorbar()

plt.grid(True, which='minor', linestyle='-', color='k', linewidth=1)
plt.axis('equal')
# plt.xticks(
#     np.arange(width) + 0.5,
#     [''.join(a_order) for a_order in permutations('123456', 5)],
#     size=4,
#     rotation='vertical',
# )
# plt.yticks(
#     np.arange(width) + 0.5,
#     [''.join(b_order) for b_order in permutations('123456', 5)],
#     size=4,
#     rotation='vertical',
# )

plt.show()
