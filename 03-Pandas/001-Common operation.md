# 行列操作
## 删除
* 删除列```axis = 1```
* 删除行```axis = 0``` （默认）
* 
### 列
```py
Df.drop('state',axis=1)
```
### 行
```py
df2 = df.drop(index = [611,629])
df.drop(index=['Bob', 'Dave', 'Frank'])
```
* 直接在df上做删除操作，要加上 ```inplace = True```
* ref: https://blog.csdn.net/qq_18351157/article/details/105785367

## 添加
* ref: https://www.zhihu.com/question/503434324
### 行：将一个list添加到最后一行
```py
alist=[1,2,3,4,5,6,7]
df.loc[len(df)]=alist
```

### 列
#### 将一个list添加到第x列
```py
df[0] = id
df[1] = smiless
```
#### 将一个list添加到某列（具体列名）
```py
toxicity[tox_cols[i - 1]] = predicions_n
```


#### 将一个Series添加到第x列
```py
DataFrame.insert(loc, column, value, allow_duplicates=_NoDefault.no_default)
featdf.insert(2, 'ApparentpKa', pka)
```
* pka是一个Series，尽管原来就有列头ApparentpKa，但在这里还是再写一次
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html

## 合并
### 横向合并df
```py
new_df=pd.concat([data,cal_des],axis=1)
```

## 修改列的顺序
* ref: https://blog.csdn.net/qq_40326787/article/details/107015942