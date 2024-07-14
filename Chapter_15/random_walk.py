from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]


    #计算距离和方向
    def get_step(self):
        x_direction = choice([-1, 1])
        x_distance = choice([0, 1, 2, 3, 4, 5])
        x_step = x_direction * x_distance

        y_direction = choice([-1, 1])
        y_distance = choice([0, 1, 2, 3, 4, 5])
        y_step = y_direction * y_distance

        # 计算下一个坐标在哪，用x，y列表中最后一个元素加上当前跨越的步数，计算出下一个坐标，追加到列表中
        x = self.x_values[-1] + x_step
        y = self.y_values[-1] + y_step

        self.x_values.append(x)
        self.y_values.append(y)

        return x, y

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue








