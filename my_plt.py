from matplotlib import pyplot as plt
# 设置图片的大小
fig = plt.figure(figsize=(20, 8), dpi=80)
# 数据在x轴的位置，是一个可迭代的对象
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# 数据在y轴的位置，是一个可迭代的对象，x和y轴的数据一起组成了所有要绘制出的坐标(2,15)(4,13)(6, 14.5)(8, 17)
plt.plot(x, y)
# 设置x轴的刻度
# plt.xticks(x) # 把x轴的每个数值都绘制在图上
# plt.xticks(range(2, 25))
_xtick_labels = [i/2 for i in range(4, 49)]
# plt.xticks(_xtick_labels)
plt.xticks(range(25, 50))
plt.yticks(range(min(y), max(y) + 1))
# 保存图片
#plt.savefig("./sig_size.png")
plt.show() # 展示图形
