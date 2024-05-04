import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from itertools import permutations

prop = FontProperties(fname=r'C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts\SourceHanSansSC-Regular.otf')
plt.rcParams['font.family'] = prop.get_name()

categories = [''.join(a_order) for a_order in permutations('12345')]
a_order_to_win_probability: dict = {(0, 1, 2, 3, 4): 0.7960001275104066, (0, 1, 2, 4, 3): 0.8387475222020766, (0, 1, 3, 2, 4): 0.7245083847060545, (0, 1, 3, 4, 2): 0.7758838556829692, (0, 1, 4, 2, 3): 0.8441482114397969, (0, 1, 4, 3, 2): 0.8460210679743827, (0, 2, 1, 3, 4): 0.8261650821646812, (0, 2, 1, 4, 3): 0.828476673181596, (0, 2, 3, 1, 4): 0.758115145397575, (0, 2, 3, 4, 1): 0.7626160390005492, (0, 2, 4, 1, 3): 0.7600896472980974, (0, 2, 4, 3, 1): 0.7618165659863347, (0, 3, 1, 2, 4): 0.7828157231555664, (0, 3, 1, 4, 2): 0.7871690561659405, (0, 3, 2, 1, 4): 0.7827806240082318, (0, 3, 2, 4, 1): 0.7869707443638484, (0, 3, 4, 1, 2): 0.7871215273423497, (0, 3, 4, 2, 1): 0.7869582711732981, (0, 4, 1, 2, 3): 0.8518531045579065, (0, 4, 1, 3, 2): 0.8536295307227145, (0, 4, 2, 1, 3): 0.7831523038937761, (0, 4, 2, 3, 1): 0.7390280383924555, (0, 4, 3, 1, 2): 0.7856708315947274, (0, 4, 3, 2, 1): 0.7400798030554858, (1, 0, 2, 3, 4): 0.7297768875022058, (1, 0, 2, 4, 3): 0.7745373499283383, (1, 0, 3, 2, 4): 0.7305557838252829, (1, 0, 3, 4, 2): 0.7766959993613329, (1, 0, 4, 2, 3): 0.8453010966006791, (1, 0, 4, 3, 2): 0.8469705622165289, (1, 2, 0, 3, 4): 0.7851363869389623, (1, 2, 0, 4, 3): 0.783723771396865, (1, 2, 3, 0, 4): 0.7854265959827168, (1, 2, 3, 4, 0): 0.7846586122429999, (1, 2, 4, 0, 3): 0.7830387604484127, (1, 2, 4, 3, 0): 0.7836888315239045, (1, 3, 0, 2, 4): 0.7873663683879518, (1, 3, 0, 4, 2): 0.7873256111870774, (1, 3, 2, 0, 4): 0.7871402974784912, (1, 3, 2, 4, 0): 0.7861628947485026, (1, 3, 4, 0, 2): 0.7870820869537893, (1, 3, 4, 2, 0): 0.7861452293073503, (1, 4, 0, 2, 3): 0.8523662763444529, (1, 4, 0, 3, 2): 0.8538309390163277, (1, 4, 2, 0, 3): 0.7829877639985894, (1, 4, 2, 3, 0): 0.7376892992340589, (1, 4, 3, 0, 2): 0.7853170500752944, (1, 4, 3, 2, 0): 0.7389340614481414, (2, 0, 1, 3, 4): 0.7632972275500898, (2, 0, 1, 4, 3): 0.7616456257702096, (2, 0, 3, 1, 4): 0.763790761938379, (2, 0, 3, 4, 1): 0.763632185723025, (2, 0, 4, 1, 3): 0.7615341992868878, (2, 0, 4, 3, 1): 0.7630295662688213, (2, 1, 0, 3, 4): 0.7852943562448838, (2, 1, 0, 4, 3): 0.7839182448589136, (2, 1, 3, 0, 4): 0.7855716383060305, (2, 1, 3, 4, 0): 0.7848247643805288, (2, 1, 4, 0, 3): 0.7832542085046321, (2, 1, 4, 3, 0): 0.783888864247047, (2, 3, 0, 1, 4): 0.7873404081324368, (2, 3, 0, 4, 1): 0.7871770265264305, (2, 3, 1, 0, 4): 0.7871496923464936, (2, 3, 1, 4, 0): 0.7862133231984487, (2, 3, 4, 0, 1): 0.7869144419155611, (2, 3, 4, 1, 0): 0.7861407156739095, (2, 4, 0, 1, 3): 0.783598149407871, (2, 4, 0, 3, 1): 0.7848099989551138, (2, 4, 1, 0, 3): 0.7830413535097517, (2, 4, 1, 3, 0): 0.7836579959155441, (2, 4, 3, 0, 1): 0.7851222744455615, (2, 4, 3, 1, 0): 0.7845231899668993, (3, 0, 1, 2, 4): 0.7864659483100385, (3, 0, 1, 4, 2): 0.7864096303062832, (3, 0, 2, 1, 4): 0.7864194512691609, (3, 0, 2, 4, 1): 0.7861838583716644, (3, 0, 4, 1, 2): 0.7863469649902088, (3, 0, 4, 2, 1): 0.7861676836216023, (3, 1, 0, 2, 4): 0.7858305001892655, (3, 1, 0, 4, 2): 0.7857790922630066, (3, 1, 2, 0, 4): 0.8483760482187508, (3, 1, 2, 4, 0): 0.847380804178234, (3, 1, 4, 0, 2): 0.7853554677047807, (3, 1, 4, 2, 0): 0.7841912345091842, (3, 2, 0, 1, 4): 0.7856490384820877, (3, 2, 0, 4, 1): 0.7854375325609397, (3, 2, 1, 0, 4): 0.8482278486919296, (3, 2, 1, 4, 0): 0.8472524309587878, (3, 2, 4, 0, 1): 0.7849739490798573, (3, 2, 4, 1, 0): 0.7839891723396735, (3, 4, 0, 1, 2): 0.7855381006260274, (3, 4, 0, 2, 1): 0.7853780053255659, (3, 4, 1, 0, 2): 0.7851765307046075, (3, 4, 1, 2, 0): 0.7840374113159407, (3, 4, 2, 0, 1): 0.7849304211267303, (3, 4, 2, 1, 0): 0.7839508395943606, (4, 0, 1, 2, 3): 0.8532167495099214, (4, 0, 1, 3, 2): 0.8547502670513398, (4, 0, 2, 1, 3): 0.7845961420031661, (4, 0, 2, 3, 1): 0.7405174075101744, (4, 0, 3, 1, 2): 0.7866502606443962, (4, 0, 3, 2, 1): 0.741327900837754, (4, 1, 0, 2, 3): 0.8526154979018743, (4, 1, 0, 3, 2): 0.8540354490816442, (4, 1, 2, 0, 3): 0.8462056438119328, (4, 1, 2, 3, 0): 0.803250433539525, (4, 1, 3, 0, 2): 0.7855101070635326, (4, 1, 3, 2, 0): 0.7342529147486302, (4, 2, 0, 1, 3): 0.7836606929711109, (4, 2, 0, 3, 1): 0.7848622419536346, (4, 2, 1, 0, 3): 0.8460375591300009, (4, 2, 1, 3, 0): 0.8428677347169471, (4, 2, 3, 0, 1): 0.7851702954004522, (4, 2, 3, 1, 0): 0.7801447420951299, (4, 3, 0, 1, 2): 0.7872914620142022, (4, 3, 0, 2, 1): 0.7871688363784406, (4, 3, 1, 0, 2): 0.7870958748158017, (4, 3, 1, 2, 0): 0.7817967587595782, (4, 3, 2, 0, 1): 0.7869188438867903, (4, 3, 2, 1, 0): 0.7817412938823267}

values = [a_order_to_win_probability[a_order] for a_order in permutations(range(5))]

plt.bar(categories, values, color='skyblue')

plt.title('所有120种可能的出场顺序对应的A队获胜概率')
plt.xlabel("A队出场顺序")
plt.ylabel('A队获胜概率')
plt.xticks(rotation='vertical', size='x-small')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
