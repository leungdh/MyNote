# python ndarray与pandas series相互转换，ndarray与dataframe相互转换

* ref：https://blog.csdn.net/qq_33873431/article/details/98077676

```py
# Series to 1darray
series = df['pka']
array = series.values


#1darray to series
data = np.array([1, 2, 3])
ser = pd.Series(data.tolist())
```