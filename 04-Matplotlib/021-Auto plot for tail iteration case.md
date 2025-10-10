```py
# 自动化绘图函数
def plot_violin_by_tail_id(df, tailid, fixed_values_template, range_variable_index, range_values, xlabel, ylabel):
    """
    自动生成 violinplot，根据指定的 Tail_ID 和模式生成数据。
    - df: 数据框
    - tailid: 要筛选的 Tail_ID
    - fixed_values_template: 固定部分的模板列表 (如 [4, 0, 0, 0])
    - range_variable_index: 可变部分索引 (如 1 表示修改第 2 项)
    - range_values: 可变部分的范围 (如 [1, 2, 3, ..., 10])
    - xlabel: x 轴标签
    - ylabel: y 轴标签
    """
    # 更新固定模板，生成 box_data 和 labels
    box_data = []
    valid_means = []  # 存储非空列表的均值
    for val in range_values:
        template = fixed_values_template.copy()
        template[range_variable_index] = val
        filtered_data = filter_by_tail_id(df, tailid, template)['epo.prob.clf1.0'].tolist()
        box_data.append(filtered_data)
        # 计算均值，跳过空列表
        if filtered_data:
            valid_means.append(sum(filtered_data) / len(filtered_data))
        else:
            valid_means.append(None)  # 使用 None 作为占位符
    
    # 设置标签
    labels = [str(val) for val in range_values]
    
    # 绘图
    sns.violinplot(data=box_data, 
                   palette=sns.color_palette(palette='Paired'),
                   inner=None, linewidth=0)
    
    # 添加均值点，跳过 None 值
    for idx, mean in enumerate(valid_means):
        if mean is not None:
            plt.scatter(x=idx, y=mean, color='white', zorder=3)
    
    # 设置图形属性
    plt.xticks(ticks=range(len(box_data)), labels=labels, fontsize=11)
    plt.ylim(0, 1)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(tailid, fontsize=14)
    plt.show()

# 使用示例
tailid = 'T4B2'
df = pd.read_excel(r'/data3/liangdh/project/alnp/Lipid5Se_20241218.all.predprop.xlsx')
plot_violin_by_tail_id(
    df=df,
    tailid=tailid,
    fixed_values_template=[4, 0, 0, 0],  # 模板
    range_variable_index=1,  # 可变部分索引
    range_values=range(1, 11),  # 变化范围 1-10
    xlabel='Length of the 2nd C',
    ylabel='Probability of EPO>MC3'
)

```