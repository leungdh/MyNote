```py
cmap = LinearSegmentedColormap.from_list("RedBlue", ["red", "blue"])
cmap = sns.color_palette("coolwarm",as_cmap=True)
```

```py
df_temp = df_dict[subgroup][['Group']+[col for col in df_data1_sortmean.columns.tolist()if col.startswith(item)]+['stateScore']].dropna()
min_score = df_temp['stateScore'].min()
max_score = df_temp['stateScore'].max()
for idx, row in df_temp.iterrows():
    # 画折线图用的数据
    values = row.iloc[1:5].values
    # 获取对应的stateScore（要依据score做渐变色）
    score = row['stateScore']
    # 将score归一化到0-1范围，用于颜色映射
    norm_score = (score - min_score) / (max_score - min_score)
    # 获取对应的颜色
    color = cmap(norm_score)
    # 绘制折线
    plt.plot(values, color=color, linewidth=1, alpha=0.8,marker='o',label = row['Group'])

# 添加颜色条作为参考
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min_score, vmax=max_score))
sm.set_array([])
# 明确指定使用当前坐标轴来放置颜色条
cbar = plt.colorbar(sm, ax=plt.gca())
cbar.set_label('stateScore')
```