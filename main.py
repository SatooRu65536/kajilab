import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def integral(x):
    dx = []
    sum = 0
    for i in range(len(x)):
        sum += x[i] * 0.01
        dx.append(sum)
    return dx


# CSVファイルのパス
csv_file_path = "./log/iphone-2.csv"

# CSVファイルを読み込む
data = pd.read_csv(csv_file_path)

# 時間、X軸、Y軸、Z軸のデータを取得
time = data['time']
x = data['x'].values
y = data['y'].values
z = data['z'].values

# 積分したデータを格納するリスト
dx = integral(x)
d2x = integral(dx)

# グラフの描画
fig = plt.figure(figsize=(30, 20))

ax1 = fig.add_subplot(3, 1, 1)
ax1.grid(color='k', linestyle='dotted', linewidth=1, alpha=0.5, zorder=2)
ax1.set_title('加速度', fontdict={'size': 14})
ax1.set_xlabel('時間[s]', fontdict={'size': 10})
ax1.set_ylabel('加速度[m/s^2]', fontdict={'size': 10})

ax2 = fig.add_subplot(3, 1, 2)
ax2.grid(color='k', linestyle='dotted', linewidth=1, alpha=0.5, zorder=2)
ax2.set_title('速度', fontdict={'size': 14})
ax2.set_xlabel('時間[s]', fontdict={'size': 10})
ax2.set_ylabel('速度[m/s^2]', fontdict={'size': 10})

ax3 = fig.add_subplot(3, 1, 3)
ax3.grid(color='k', linestyle='dotted', linewidth=1, alpha=0.5, zorder=2)
ax3.set_title('距離', fontdict={'size': 14})
ax3.set_xlabel('時間[s]', fontdict={'size': 10})
ax3.set_ylabel('距離[m]', fontdict={'size': 10})

# データをプロット
ax1.plot(time, x, label='ax1')
ax2.plot(time, dx, label='vx')
ax3.plot(time, d2x, label='px')

# 範囲を指定
fig_range  = (0.5, 4)
ax1.set_xlim(*fig_range)
ax2.set_xlim(*fig_range)
ax3.set_xlim(*fig_range)

ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=8)
ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=8)

# グラフを表示
plt.show()
