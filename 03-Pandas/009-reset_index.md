# 重置index序号排序

* ref：https://blog.csdn.net/xiewenrui1996/article/details/109055070
* `drop=True`:index这列不新建为一列
* `inplace = True`:在原df上修改
```py
t12_pka = t12.drop(index = loc,axis = 0)
t12_pka.reset_index(drop=True, inplace = True)
```