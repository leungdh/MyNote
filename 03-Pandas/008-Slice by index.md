
### 索引值
```py
df.loc[18,'Structure']
```
输出
```py
nan
```

### 索引某些行所有列
```py
df.loc[[611,629]]
```
输出
```py
    ABOF Code 订单编号 Structure Medicilion_ID  Size （nm）  PDI  EE%  \
611  NaN  NaN  NaN       NaN           NaN        NaN  NaN  NaN   
629  NaN  NaN  NaN       NaN           NaN        NaN  NaN  NaN   

     mRNA的浓度（ug/ml)or mg/ml  ApparentpKa  ...  pKa Salt_Coefficients  \
611                     NaN          NaN  ...  NaN               NaN   
629                     NaN          NaN  ...  NaN               NaN   

    Stereo_Chemistry Chemist NoteBook_Number Shipment_Date HNMR  LCMS CAD/min  \
611              NaN     NaN             NaN           NaN  NaN   NaN     NaN   
629              NaN     NaN             NaN           NaN  NaN   NaN     NaN   

    Unnamed: 24  
611         NaN  
629         NaN  

```