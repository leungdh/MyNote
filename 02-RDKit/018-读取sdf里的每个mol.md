```py
all_sdf = [ x for x in Chem.ForwardSDMolSupplier(sdffile) if x is not None]
```