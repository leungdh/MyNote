select row that contains specifit list element
依据列表选择含列表元素的行
```py
df_sel = df[df['Whole.SMILES'].isin(select_smill)]
```