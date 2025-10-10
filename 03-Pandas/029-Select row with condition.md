Select row with condition
挑选符合条件的行
```py
for head_type in df_sel['HeadType'].unique():
    mask = df_sel['HeadType'] == head_type  # 挑选
    df_head_sel = df_sel[mask]

```
