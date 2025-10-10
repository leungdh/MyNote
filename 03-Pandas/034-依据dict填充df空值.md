```py
filename = r'C:/Users/danhong.liang/hong/02Chemistry/00Result/25-0401-0110+0228-EPO-xc/AG系列新脂质20250228-M.xlsx'

df = pd.read_excel(filename)

mapping = pd.read_excel(r'C:/Users/danhong.liang/hong/01LNP/id_ab_mapping_add.xlsx')
id2abcode = dict(zip(mapping['Compound_ID'].astype(str),mapping['AB_Code']))
df['AB_Code'] = df['Compound_ID'].fillna(df['Compound_ID'].map(id2abcode))
```