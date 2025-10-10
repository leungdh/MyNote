### 设置label字体大小 坐标轴字体大小
```py
plt.xlabel('AGILE S2 Diversity', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
```

## 可能还想看
### 设置坐标轴范围
```py
plt.ylim(0, 0.3)
```

### 设置坐标轴刻度
* https://blog.csdn.net/HHG20171226/article/details/101294381
```py
#设置坐标轴刻度，从3到14，间隔为1
my_x_ticks = np.arange(3, 14, 1)
plt.xticks(my_x_ticks)
```
