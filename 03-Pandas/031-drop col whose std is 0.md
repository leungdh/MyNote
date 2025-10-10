删除df中列值一致的列
```py
df_feas.drop(df_feas.columns[df_feas.std()==0],axis=1,inplace = True)

```
