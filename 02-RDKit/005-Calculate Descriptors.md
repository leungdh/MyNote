# 计算描述符

## 常计算的项目
MolWt
MolLogP

## 演示
```py
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors


mol=Chem.MolFromSmiles('CCC')
des_list=[x[0] for x in Descriptors._descList]
calculator = MoleculeDescriptors.MolecularDescriptorCalculator(des_list)
each_des = calculator.CalcDescriptors(mol)
```

## ref: 

https://zhuanlan.zhihu.com/p/141440170
