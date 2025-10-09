# ECFP MorganFP

* 在RDKit里面算ECFP用的是MorganFP
* 参数
  * radius = 2
  * nBits = 2048
* 要用AllChem去调用GetMorganFingerprintAsBitVect要不然会报错
```py
from rdkit.Chem import AllChem
morgan_bitvect = AllChem.GetMorganFingerprintAsBitVect(mols[0], 2, 2048)
```

```py
fps = [AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(smi), 2, 4096)for smi in tmp['Whole.SMILES']]
```

* FCFP: useFeatures=True

* ref: https://zhuanlan.zhihu.com/p/86701228