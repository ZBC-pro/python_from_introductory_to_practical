import plotly.express as px
from Chapter_15.die import Die

die_1 = Die()
die_2 = Die()

# results = []
# for roll_num in range(1000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)
#简写for循环列表
results = [die_1.roll() * die_2.roll() for _ in range(1000)]

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in poss_results]

title = "Results of Rolling D6*D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#对图标不满意的地方进行修正   xaxis_dtick指定x轴刻度上的间距并在每个x轴上的每个柱子都有标签
fig.update_layout(xaxis_dtick=1)

fig.show()