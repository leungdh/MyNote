

## 设置属性：mol.SetProp

## SetProp
```py
import os
from rdkit import Chem

os.chdir(r'C:\Users\danhong.liang\hong\01LNP\cal_siml_temp')
path = r'C:\Users\danhong.liang\hong\01LNP\cal_siml_temp'
files = os.listdir(path)
database = []

for f in files:
    mol = Chem.MolFromMolFile(f)
    mol.SetProp('_Name',f[:-4])
    database.append(mol)
```

## GetProp
```py
molname = mol.GetProp('_Name')
```