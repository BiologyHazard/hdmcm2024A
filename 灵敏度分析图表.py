import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from itertools import permutations

prop = FontProperties(fname=r'C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts\SourceHanSansSC-Regular.otf')
plt.rcParams['font.family'] = prop.get_name()

categories = [f'21:{x}' for x in range(20)]
data = [0.9294434288688824, 0.9259438711081995, 0.9223569685634713, 0.9186860425621115, 0.9149345540985088, 0.9111060777055666, 0.9072042765888855, 0.9032328791717112, 0.8991956571562925, 0.8950964051699295,
        0.8909389220316573, 0.8867269936478718, 0.8824643775220637, 0.8781547888446937, 0.8738018881138638, 0.8694092702253287, 0.8649804549611944, 0.861369500014191, 0.8591742648407323, 0.8569677695331432]


plt.plot(categories, data, color='skyblue')

plt.title('修改历史数据后的A队最高获胜概率')
plt.xlabel("历史数据")
plt.ylabel('A队最高获胜概率')
plt.xticks(rotation='vertical')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
