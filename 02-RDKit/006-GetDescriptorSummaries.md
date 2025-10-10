# 获取描述符的描述

```py
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
des_list = [x[0] for x in Descriptors._descList]
calculator = MoleculeDescriptors.MolecularDescriptorCalculator(des_list)


import pandas as pd
df = pd.DataFrame()
name = calculator.GetDescriptorNames()
summary = calculator.GetDescriptorSummaries()
df['Name'] = name
df['Des'] = summary
print(df)
```




## ref: 

调出描述符的描述：https://zhuanlan.zhihu.com/p/141440170

各特征的官方参考来源：https://rdkit.org/docs/GettingStartedInPython.html#list-of-available-descriptors
