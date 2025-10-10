# df.to_csv
* index = None：不要将0,1,2,3，。。。保存为第一列
* header = None：不要将0,1,2,3，。。。保存为表头（第一行）。但有时候会有自定义的表头，则不要加上这一句。
```py
df.to_csv('../../test/ori3.csv',header = None, index = None)
```

# pd.read_csv
* 如果要读取的csv文件没有表头，则要加上header = None，否则第一行数据会变成表头
```py
df = pd.read_csv('ori3.csv',header = None)
```