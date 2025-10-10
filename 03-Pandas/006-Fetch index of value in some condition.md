

example:
```py
t = pd.Series([1,2,4,5,3,7,36,45,65,23,77])
t[t>10].index
```
out:
```py
Int64Index([6, 7, 8, 9, 10], dtype='int64')
```

* t>10: 返回True或False的Series（全部）
* t[t>10]：返回值大于10的部分Series
* t[t>10].index：返回值大于10的部分Series的Index