依据dict填充df空值
```py
filename = r'C:/path/excel.xlsx'

df = pd.read_excel(filename)

mapping = pd.read_excel(r'C:/path/id_ab_mapping_add.xlsx')
id2abcode = dict(zip(mapping['Compound_ID'].astype(str),mapping['AB_Code']))
df['AB_Code'] = df['Compound_ID'].fillna(df['Compound_ID'].map(id2abcode))

```

