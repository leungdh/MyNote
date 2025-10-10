Read sdf into mols 读取sdf里的每个mol
```py
all_sdf = [ x for x in Chem.ForwardSDMolSupplier(sdffile) if x is not None]

```
