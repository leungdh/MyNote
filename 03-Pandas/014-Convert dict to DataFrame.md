## 把dict变成DataFrame

```py
d_mol = {}
for i in range(0,len(all_sdf)):
    mol = all_sdf[i]
    dictinfo = mol.GetPropsAsDict()
    d_mol[i]=dictinfo
```