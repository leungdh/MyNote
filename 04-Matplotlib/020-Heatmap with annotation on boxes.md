```py
import os
import pandas as pd
from scipy.stats import spearmanr, pearsonr
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
import itertools
from matplotlib.ticker import MaxNLocator
```

```py
def plot_scatter(df,feature,save_name, r, p):
    plt.figure(figsize=(5, 4),dpi=100)
    plt.scatter(df[fea], df[PROP],alpha=0.4)
    plt.title("Se-Series Features")
    plt.xlabel(save_name.split("/")[-1].split(".png")[0])
    plt.ylabel(PROP)
    labels = df['Compound_ID'].tolist()
    plt.annotate(f"R = {r:.2f}\np-value = {p:.2e}",xy=(-0.05, 1.05), xycoords='axes fraction')
    for i, label in enumerate(labels):
        plt.annotate(label, (df[fea][i],df[PROP][i]))
    plt.savefig (save_name, bbox_inches='tight')         
    plt.close()
    

def corr_pval(x, y):
    r, p = pearsonr(x, y)
    return r, p
```

```py
PROP = 'ApparentpKa'
corr_matrix_r = pd.DataFrame(index=feature_cols, columns=['all', 'head1', 'head2', 'head3', 'head4','head5',
                                                           'head6', 'head7', 'tail1','tail2','tail3', 'tail4','tail5', 
                                                          'tail6','tail7','tail8','tail9','tail10'])
corr_matrix_p = pd.DataFrame(index=feature_cols, columns=['all', 'head1', 'head2', 'head3', 'head4','head5',
                                                           'head6', 'head7', 'tail1','tail2','tail3', 'tail4','tail5', 
                                                          'tail6','tail7','tail8','tail9','tail10'])

for fea in feature_cols:
    df_sel = df
    if "macro" in fea.lower():
        df_sel = df_sel[df_sel[fea]!=30]
        df_sel.reset_index(drop = True, inplace = True)
    if "len" in fea.lower() or "distance" in fea.lower():
        df_sel = df_sel[df_sel[fea]!=100]
        df_sel.reset_index(drop = True, inplace = True)
    if len(df_sel) >= 2:
        r, p = corr_pval(df_sel[fea], df_sel[PROP])
        corr_matrix_r.loc[fea, 'all'] = r
        corr_matrix_p.loc[fea, 'all'] = p
        png_name = f"/data3/liangdh/project/alnp/png/huanji/Se_apka/{fea}.png"
        plot_scatter(df_sel, fea, png_name, r, p)
        

        for head_type in df_sel['HeadType'].unique():
            mask = df_sel['HeadType'] == head_type
            try:
                r, p = corr_pval(df_sel[fea][mask], df_sel[PROP][mask])
                corr_matrix_r.loc[fea, f'head{head_type}'] = r
                corr_matrix_p.loc[fea, f'head{head_type}'] = p
                df_head_sel = df_sel[mask]
                df_head_sel.reset_index(drop = True, inplace = True)
                png_name = f"/data3/liangdh/project/alnp/png/huanji/Se_apka/{fea}_head{head_type}.png"
                plot_scatter(df_head_sel, fea, png_name, r, p)
            except Exception as e:
                pass
#                 print(e)

        for tail_type in df_sel['TailType'].unique():
            mask = df_sel['TailType'] == tail_type
            try:
                r, p = corr_pval(df_sel[fea][mask], df_sel[PROP][mask])
                corr_matrix_r.loc[fea, f'tail{tail_type}'] = r
                corr_matrix_p.loc[fea, f'tail{tail_type}'] = p
                df_tail_sel = df_sel[mask]
                df_tail_sel.reset_index(drop = True, inplace = True)
                png_name = f"/data3/liangdh/project/alnp/png/huanji/Se_apka/{fea}_tail{tail_type}.png"
                plot_scatter(df_tail_sel, fea, png_name,r, p)
            except Exception as e:
                pass
#                 print(e)


```

```py
corr_matrix_r = corr_matrix_r.dropna(how='all').dropna(axis=1, how='all')
corr_matrix_filled_r = corr_matrix_r.fillna(0)

corr_matrix_p = corr_matrix_p.dropna(how='all').dropna(axis=1, how='all')
corr_matrix_p_float = corr_matrix_p.astype(float).round(2)
corr_matrix_filled_p = corr_matrix_p_float.fillna('-')

plt.figure(figsize=(20, 15))
sns.heatmap(corr_matrix_filled_r.astype(float), annot=corr_matrix_filled_p, fmt="", 
            cmap='coolwarm', 
            cbar=True, annot_kws={"size": 12})
plt.title("Correlation Matrix with p-values on "+PROP, size= 15)
plt.show()
```
