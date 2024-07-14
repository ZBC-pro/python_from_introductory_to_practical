import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    #fig, ax = plt.subplots()
    #可以调节maplote输出的尺寸大小和分辨率，在subplots
    #fig, ax = plt.subplots(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)

    #ax.scatter(rw.x_values, rw.y_values, s=15)
    #range(rw.num_points)等同于range(0,5000),定义后的num_points是5000，他会生成一个0~4999的列表，列表长度就是游走点的个数
    #将point_numbers赋给c，这就表示这个图会根据point_numbers中数字在列表的位置变化颜色，而不是像前面那样根据y_values的值大小去变色
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,    #颜色越来越深可以是plt.cm.viridis
               edgecolors='none', s=1)
    ax.set_aspect('equal')

    #确定起始点  绿色绘制起点，红色绘制终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Press enter 'q' to break: ")
    if keep_running == 'q':
        break



