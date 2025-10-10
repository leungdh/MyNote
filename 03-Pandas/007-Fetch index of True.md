# 获取True的索引

```py
ll = df['ApparentpKa'].isnull().values.tolist()
loc = [i for i,x in enumerate(ll) if x]
```

* ref: https://www.coder.work/article/80424#google_vignette