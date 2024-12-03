import numpy as np
import matplotlib.pyplot as plt

# 设置 x 的取值范围从 -2π 到 2π，间隔为 0.1
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 计算 y = sin(x)
y = np.sin(x)

# 绘制图像
plt.plot(x, y, label="y = sin(x)")

# 设置标题和标签
plt.title("Graph of y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")

# 显示网格
plt.grid(True)

# 显示图例
plt.legend()

# 显示图像
plt.show()
