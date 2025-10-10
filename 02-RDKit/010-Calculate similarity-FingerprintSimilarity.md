# 计算分子间的相似性-FingerprintSimilarity

### 建议直接调用TanimotoSimilarity或DiceSimilarity等算相似性的函数，而不是使用FingerprintSimilarity，以避免FP长度不一致而不自知的情况。
[计算分子间的相似性-TanimotoSimilarity](./计算分子间的相似性-TanimotoSimilarity.md)

## FingerprintSimilarity用法展示

```py
from rdkit import Chem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols

#算分子指纹
#FingerprintMol默认用的分子指纹是Chem.RDKFingerprint
#database是一个列表，放了各个分子，type: rdkit.Chem.rdchem.Mol
#并且各个分子有属性'_Name' 
fps = [FingerprintMols.FingerprintMol(mol) for mol in database]

#计算分子两两之间的相似性，并放到矩阵hmap里
#FingerprintSimilarity里的距离度量方法（metric），默认用的是DataStructs.TanimotoSimilarity
size=len(database)
hmap=np.empty(shape=(size,size))
table=pd.DataFrame()
for index, i in enumerate(fps):
    for jndex, j in enumerate(fps):
        similarity=DataStructs.FingerprintSimilarity(i, j)
        hmap[index,jndex]=similarity
        table.loc[database[index].GetProp('_Name'),database[jndex].GetProp('_Name')]=similarity
```
## 与TanimotoSimilarity的区别
### FingerprintSimilarity的源码
```py
def FingerprintSimilarity(fp1, fp2, metric=TanimotoSimilarity):
    """ returns the calculated similarity between two fingerprints,
      handles any folding that may need to be done to ensure that they
      are compatible

    """
    sz1 = fp1.GetNumBits()
    sz2 = fp2.GetNumBits()
    if sz1 < sz2:
        fp2 = FoldFingerprint(fp2, sz2 // sz1)
    elif sz2 < sz1:
        fp1 = FoldFingerprint(fp1, sz1 // sz2)
    return metric(fp1, fp2)

```
* 虽然FingerprintSimilarity在默认情况下也是调用TanimotoSimilarity做相似性计算，但它最关键的是会将FP长度不一致的情况先解决，再带相似性计算函数
* FingerprintSimilarity会自动将两个长度不一样的FP折叠（调用FoldFingerprint函数），使得两个FP长度一致后，才调用TanimotoSimilarity函数计算谷本系数。
* 如果不想用TanimotoSimilarity函数，可以设置metric=DiceSimilarity等其他相似性函数


## 相关
[为mol设置属性SetProp](./%E4%B8%BAmol%E8%AE%BE%E7%BD%AE%E5%B1%9E%E6%80%A7SetProp.md)

[RDKFingerprint](./计算分子指纹%20函数RDKFingerprint.md)

## ref
算相似性，画hmap，作聚类：https://zhuanlan.zhihu.com/p/82800978

算FP，算相似性，介绍metric：https://www.jianshu.com/p/b0148c74e85d
