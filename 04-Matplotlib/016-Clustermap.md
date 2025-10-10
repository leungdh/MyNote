```py
import seaborn as sns
sns.clustermap(df,z_score=1,cmap="vlag", center=0)
```

* cmap: 选择颜色，vlag，红蓝配色
* z_score：scale每列数据平均值到0，例如[-3,3]
* 解决坐标显示不全的参数：yticklabels=1, xticklabels = 1
