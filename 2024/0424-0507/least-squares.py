import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # 3D表示に使う
from scipy import linalg  # linalg.solve(A, b) 　Ax = bの解を求める関数

# y = w[0] + w[1]x[1] + w[2]x[2]型。
# 今回はw = [1, 2, 3]とする。
X = np.random.random((100, 2)) * 10  # 0から1*10の範囲をとる100*2の行列
y = 1 + 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100)
# x0とx1の座標からyを作成。randnで本来の値にノイズを加えている。

Xtil = np.c_[
    np.ones(X.shape[0]), X
]  # Xの行列の左端に[1,1,1,...,1]^Tを加える。(7)式を確認しよう
A = np.dot(Xtil.T, Xtil)  # 標準形A,bに当てはめる。
b = np.dot(Xtil.T, y)
w = linalg.solve(A, b)  # (8)式をwについて解く。

xmesh, ymesh = np.meshgrid(np.linspace(0, 10, 20), np.linspace(0, 10, 20))
zmesh = (w[0] + w[1] * xmesh.ravel() + w[2] * ymesh.ravel()).reshape(xmesh.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], y, color="k")
ax.plot_wireframe(xmesh, ymesh, zmesh, color="r")
plt.show()
