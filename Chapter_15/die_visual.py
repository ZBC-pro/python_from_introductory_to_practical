#Plotly Express 依赖于 pandas（一个用于高效地处理数据的库），因此需要同时安装 pandas。
#要了解使用 Plotly 可创建什么样的图形，请访问 Plotly 主页并单击 DOCS下拉菜单中的 GRAPHING LIBRARIES，
#然后单击 Python 图标或在Languages 下拉菜单中选择 Python，打开“Plotly Open Source Graphing
#Library for Python”。每个示例都包含源代码，让你知道这些图形是如何生成的。

from die import Die
import plotly.express as px

#相当于java中new了一下，创建了一个新实例
die = Die()

results = []
for roll_num in range(1000):
    #循环100次每次都调用die中的roll方法，最后存储到result中
    result = die.roll()
    results.append(result)

#分析结果  创建空列表存储每个面出现的次数
frequencies = []
#生成所有可能出现的点数1~前面定义的面数
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    #results.count(value)直接调用py的统计函数，统计出results中的各个数字包含的个数
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#print(results)

#可视化  前面的plot不同，这是一个柱状图，虽然也可以直接导入plotlylib
#plotly Express 比之前的maplotly更屌，也可以直接绘制点图或折线图，直接换调用即可
fig = px.bar(x=poss_results, y=frequencies)
fig = px.scatter(x=poss_results, y=frequencies)
fig = px.line(x=poss_results, y=frequencies)
#有关完整的图表类型清单，请单击刚才打开的“Plotly Open Source Graphing Library for Python”页面中的 PlotlyExpress。

#可视化添加各种标签
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()

