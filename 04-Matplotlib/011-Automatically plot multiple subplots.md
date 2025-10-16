
### 绘制多图与绘制单图的区别在于以下几点：
* 设定网格的行列数
* 遍历每个dataset，绘制子图
* 计算当前子图在网格中的位置
* 移除多余的子图框架
* 调整布局

```py
# 设定网格的行列数
n_rows, n_cols = 4, 7  
fig, axes = plt.subplots(n_rows, n_cols, figsize=(35, 20))
 
# 遍历每个 tailid（是一个list，略），绘制子图
for idx, tailid in enumerate(tail_ids):
    row, col = divmod(idx, n_cols)
    ax = axes[row, col]

    # 作图(随便来一个，略)
    plt.sns.violinplot(data=box_data)

# 移除多余的子图框架
for idx in range(len(tail_ids), n_rows * n_cols):
    row, col = divmod(idx, n_cols)
    axes[row, col].axis('off')

# 调整布局
plt.tight_layout()
plt.show()
```

### 完整示例1
```py
# 设定网格的行列数
n_rows, n_cols = 4, 7  
fig, axes = plt.subplots(n_rows, n_cols, figsize=(35, 20))

tail_ids = ['T1B1', 'T1B2', 'T1B3', 'T1B4', 'T2B1', 'T2B2', 'T2B3', 'T2B4', 'T3B1', 'T3B2', 'T3B3', 'T3B4', 
            'T4B1', 'T4B2', 'T4B3', 'T5B1', 'T5B2', 'T5B3', 'T6B1', 'T6B2', 'T6B3', 'T6B4', 'T7B1', 'T7B2',
            'new1', 'new2'
           ]
 
# 遍历每个 tailid，绘制子图
for idx, tailid in enumerate(tail_ids):
    # 计算当前子图在网格中的位置
    row, col = divmod(idx, n_cols)
    ax = axes[row, col]
    
    # 数据筛选并构造 box_data
    a = filter_by_tail_id(df, tailid, [1, 0, 0, 0])['epo.prob.clf1.0'].tolist()
    b = filter_by_tail_id(df, tailid, [2, 0, 0, 0])['epo.prob.clf1.0'].tolist()
    c = filter_by_tail_id(df, tailid, [3, 0, 0, 0])['epo.prob.clf1.0'].tolist()
    d = filter_by_tail_id(df, tailid, [4, 0, 0, 0])['epo.prob.clf1.0'].tolist()
    box_data = [a, b, c, d]
    labels = ['1', '2', '3', '4']
    
    # 绘制 violinplot
    sns.violinplot(data=box_data, 
                   palette=sns.color_palette(palette='Paired'),
                   inner=None, linewidth=0, ax=ax)
    
    # 在图中添加均值点
    try:
        ax.scatter(x=[0, 1, 2, 3], y=[sum(i) / len(i) for i in box_data], color='white')
    except Exception as e:
#         print(e)
        plt.scatter(x = [1,2,3], y = [ sum(i)/len(i) for i in box_data[1:]], color = 'white')
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Length of the 1st C', fontsize=12)
    ax.set_ylabel('Probability of EPO>MC3', fontsize=12)
    ax.set_title(tailid, fontsize=14)

# 移除多余的子图框架
for idx in range(len(tail_ids), n_rows * n_cols):
    row, col = divmod(idx, n_cols)
    axes[row, col].axis('off')

# 调整布局
plt.tight_layout()
# plt.savefig("grid_violin_plot.png", dpi=300)
plt.show()

```

### 完整实例2
```py
n_rows, n_cols = len(df15.groupby('Biochem')), len(cytokine_cols)
fig, axes = plt.subplots(n_rows, n_cols, figsize=(70, 7))

for i,(g,group_df) in enumerate(df15.groupby('Biochem')):
    # 计算当前子图在网格中的位置
    row=i
    for j,c_col in enumerate(cytokine_logcols):
        col = j
        ax = axes[row, col]
        
        # 获取子图数据
        group_df_selcol = group_df[['Compound_ID',c_col,'TLR2.box1.affinity.energy']]
        df_sel = group_df_selcol[(~group_df_selcol[c_col].isna())&(~group_df_selcol['TLR2.box1.affinity.energy'].isna())
                         &(~group_df_selcol.isin([-np.inf]).any(axis=1))]
        df_sel.reset_index(drop=True, inplace = True)
        id_list = df_sel['Compound_ID'].tolist()
        
        # 绘制子图
        ax.scatter(df_sel['TLR2.box1.affinity.energy'],df_sel[c_col],alpha = 0.3)
        ax.set_xlabel("TLR2.box1.affinity.energy",fontsize = 10)
        ax.set_ylabel(c_col,fontsize = 10)
        ax.set_title(g,fontsize = 10)
        try:
            corr,pvalue = pearsonr(df_sel['TLR2.box1.affinity.energy'],df_sel[c_col])
            ax.annotate(f"pcc = {corr:.2f}\npvalue = {pvalue:.2e}",xy=(-0.15, 1.15), xycoords='axes fraction')
        except:
            pass
        
#         print(row,col,'\n',g, '\n',c_col)
#         display(df_sel[['Compound_ID',c_col,'TLR2.box1.affinity.energy']])
        
plt.tight_layout()
plt.show()
```


### 完整实例3
```py
for subgroup in df_dict.keys():
    n_rows, n_cols = 4, 4  
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(30, 18))
    for idx,item in enumerate(items):
        row, col = divmod(idx, n_cols)
        ax = axes[row, col]
        df_temp = df_dict[subgroup][['Group']+[col for col in df_data1_sortmean.columns.tolist()if col.startswith(item)]+['stateScore']].dropna()
#         display(df_temp)
        min_score = df_temp['stateScore'].min()
        max_score = df_temp['stateScore'].max()
        for _, df_row in df_temp.iterrows():
            # 获取时间点数据（前4列）
            values = df_row.iloc[1:5].values
            # 获取对应的stateScore
            score = df_row['stateScore']

            # 将score归一化到0-1范围，用于颜色映射
            norm_score = (score - min_score) / (max_score - min_score)

            # 获取对应的颜色
            color = cmap(norm_score)

            # 绘制折线
            ax.plot(values, color=color, linewidth=1, alpha=0.8,marker='o',label = df_row['Group'])

        # 添加颜色条作为参考
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min_score, vmax=max_score))
        sm.set_array([])
        # 明确指定使用当前坐标轴来放置颜色条
        cbar = plt.colorbar(sm, ax=ax)
        cbar.set_label('stateScore')

        ax.set_xticks(ticks=[0, 1, 2, 3], labels=['Dose 1','Dose 2','Dose 3','Dose 4'])
        ax.set_ylabel(item,size = 20)
        ax.set_title(subgroup)
        ax.legend()
        
        
    # 调整布局
    plt.tight_layout()
    # plt.savefig("grid_violin_plot.png", dpi=300)
    plt.show()

```

### Example 4
```py
n_rows, n_cols = 2, 4
fig,axes = plt.subplots(n_rows, n_cols, figsize = (15,6))

for idx, (num1, df_temp1) in enumerate(df_lipid5_mc3.iloc[2:,].groupby('制剂订单编号')):

    # 计算子图位置
    row, col = divmod(idx, n_cols)
    ax = axes[row, col]
    
#     plt.figure(figsize=(4,3),dpi=120)
    for lipid, df_temp2 in df_temp1.groupby('Compound_ID'):
        ax.plot([1,2],df_temp2['IL-6 pg/ml'],label = lipid,marker = 'o')
    ax.set_xticks([1,2],df_temp1['生物活性订单编号'].unique().tolist())
    ax.set_title(num1)
    ax.set_ylabel('IL-6 pg/mL')
    ax.legend()
    ax.set_ylim([0,240])

# 移除多余的子图框架
for idx in range(len(df_lipid5_mc3.iloc[2:,].groupby('制剂订单编号')), n_rows * n_cols):
    row, col = divmod(idx, n_cols)
    axes[row, col].axis('off')    

plt.tight_layout()
plt.show()
```

