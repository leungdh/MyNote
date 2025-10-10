
```py
x = df[col].tolist()
log_data = np.log10(x)
figure = plt.figure(figsize=(6,5))
bins = np.logspace(np.log10(10**5), np.log10(10**11), num=20)
weights = np.ones_like(x)/float(len(x))
plt.hist(x = x, weights = weights, bins= bins, edgecolor = 'white')

# 设置图表标题和轴标签
plt.xlabel(col+' Total Flux', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0, 0.2)
plt.xscale('log')
# 显示图表
plt.plot()

```

* np.log10(data)：对数据进行对数变换。
* np.logspace(np.log10(10**5), np.log10(10**11), num=20)：创建对数间隔的 bins 区间，num=20 指定了直方图的条数。你可以根据数据的具体分布调整 num 的值。
* plt.xscale('log') 设置对数尺度的x轴

## 对数尺度
```py
bins = np.logspace(np.log10(10**5), np.log10(10**11), num=20)
```
* 并不是将区间划分为 20 等分，而是根据对数尺度在区间 [10^5, 10^11] 上生成 20 个对数均匀分布的点。
* np.log10(10**5) 和 np.log10(10**11) 分别是对数尺度下的起始和结束值，它们是 5 和 11。
    * 也就是说，np.logspace(np.log10(10**5), np.log10(10**11), num=20) 在对数范围 [5, 11] 上生成 20 个等间距的点。
* 这些点是按照对数尺度均匀分布的，而不是在实际数值（如 10^5 到 10^11）上划分成等距的区间。
* 这些点在对数尺度上是等间距的，但是它们在数值尺度上并不是等间隔的。换句话说，数值间的差距随着数值的增大而增大。这是因为我们在对数尺度上进行均匀分布，所以对数尺度上的间隔是固定的，这也是为什么要设置对数尺度的x轴（plt.xscale('log') ）
* 