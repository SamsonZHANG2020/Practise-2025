import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 读取TXT文件
file_path = "Raman spectra 1.txt"
data = np.loadtxt(file_path,)  # 假设每行数据由空格分隔 #delimiter=' '

# 解析数据
x_data = data[:, 0]
y_data = data[:, 1]

# 绘制图形
plt.plot(x_data, y_data, c='green')
plt.xlabel("Raman(cm-1)",fontsize=16)
plt.ylabel("Intensity(a.u.)",fontsize=16)
plt.title("Raman spectra 1 349.5_416.5",fontsize=20)
plt.axis([300, 500, 500, 15000])
plt.yticks([])
plt.tick_params(axis='both',which='major',labelsize=14)

x_major_locator=MultipleLocator(25)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)

plt.show()

