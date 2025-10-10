# 计算分子间的相似性-TanimotoSimilarity

## TanimotoSimilarity用法介绍
```py
from rdkit import Chem,DataStructs
mol1 = Chem.MolFromSmiles("CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O")
mol2 = Chem.MolFromSmiles("COC1=C(C=CC(=C1)C=O)O")
fp1 = Chem.RDKFingerprint(mol1)
fp2 = Chem.RDKFingerprint(mol2)
print "fingerprint similarity: ",DataStructs.TanimotoSimilarity(fp1,fp2)
```
The output is
```
RDK fingerprint: 0.471502590674
```

## 相关
[RDKFingerprint](./计算分子指纹%20函数RDKFingerprint.md)

[FingerprintSimilarity](./计算分子间的相似性-FingerprintSimilarity.md)：这边介绍了TanimotoSimilarity和Fingerprint的区别

## ref:
https://www.researchgate.net/post/How_to_compare_a_set_of_SMILES_structures

