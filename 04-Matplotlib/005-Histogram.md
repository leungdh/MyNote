# 直方图 Histogram


## plt.hist(x = data,bins)
* data中存放的是数据的值，如相似度
* bins设置按照什么样的区间划分data
* 如按照0~0.1, 0.1~0.2, 0.2~0.3, ..., 0.9~1.0, 1.0~1.1划分
  * bins = np.arange(0,1.2,0.1)
  * 注意：最后一个区间是[1.0,1.1]，其他的区间是[0,0.1), [0.1,0.2) , ...
```py
bins = np.arange(0,1.2,0.1)
plt.hist(x = each_sim, bins= bins)
```
* 如果想让y轴显示每个区间出现的频率（概率）则加上weights
```py
weights = np.ones_like(each_sim)/float(len(each_sim))
plt.hist(x = each_sim, weights = weights, bins = bins)
```

## 完整示例
```py
import matplotlib.pyplot as plt

color = '#1f77b4'

figure = plt.figure(figsize=(6,5))
bins = np.arange(0,1.2,0.1)
weights = np.ones_like(each_sim)/float(len(each_sim))
plt.hist(x = each_sim, weights = weights, bins= bins, color = color, edgecolor = 'white')

# 设置图表标题和轴标签
plt.xlabel('AGILE S2 Similarity', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0, 0.3)
# 显示图表
plt.plot()
plt.savefig('agileS2_fp1024_rdkit_sim_1.png',dpi = 300)
```

## 多组直方图/堆积直方图
* 比单直方图不同的是x, weights, labels，colors（如有）需要输入列表
```py
x = [sim_value,sim_value[:1330]]
labels = ['66','30']
weights = [np.ones_like(sim_value)/float(len(sim_value)),np.ones_like(sim_value[:1330])/float(len(sim_value[:1330]))]
```
### 示例
```py
import matplotlib.pyplot as plt
import numpy as np
x = [sim_value,sim_value[:1330]]
labels = ['66','30']
bins = np.arange(0,1.1,0.1)
plt.style.use('seaborn')
plt.figure(figsize=(6,5),dpi = 150)
weights = [np.ones_like(sim_value)/float(len(sim_value)),np.ones_like(sim_value[:1330])/float(len(sim_value[:1330]))]
plt.hist(x, bins = bins, weights = weights,
         edgecolor = 'white',label = labels, stacked=False)
plt.ylim(0,0.3)
plt.legend(loc = 'upper right')
plt.xlabel('Fingerprint Similarity',fontsize = 15)
plt.ylabel('Frequency',fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.show()
```


## ref
设置weights：https://blog.csdn.net/crazy_scott/article/details/84395239

其他显示频率的方法：https://blog.csdn.net/qq_40344897/article/details/116097188

多组直方图：https://blog.csdn.net/weixin_46707493/article/details/119832774