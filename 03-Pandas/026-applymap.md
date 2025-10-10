
* While apply modify a column of a DataFrame, applymap can modify a whole DataFrame
```py
df_feas.applymap(lambda x: 1 if x >0 else 0)

```
