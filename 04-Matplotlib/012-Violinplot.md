```py
import seaborn as sns
box_data = [ori_similist, genmol_similist, agile_similist]
palette = ["lightskyblue", "salmon","turquoise"]

sns.violinplot(box_data, palette = palette, inner = None, linewidth = 0)
plt.scatter(x = [0,1,2], y = [ sum(i)/len(i) for i in box_data], color = 'white')
plt.xticks(ticks = [0, 1, 2], labels = labels, fontsize = 11)

```

* ref:
* https://www.jianshu.com/p/b3aba687995d
* https://seaborn.pydata.org/generated/seaborn.violinplot.html