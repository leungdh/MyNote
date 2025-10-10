# Write sdf 写sdf格式的分子

每个写进一个sdf
```py
os.chdir(savepath)
for i, mol in enumerate(all_sdf):
    writer = Chem.SDWriter(sdf_name[i])
    all_sdf[i].SetProp('_Name', sdf_name[i])
    writer.write(mol)
    writer.close()
```

多个写进一个sdf
```py
for i, smi in enumerate(smi_series):
    mol = Chem.MolFromSmiles(smi)
    mol.SetProp("_Name",str(df.index[i]))
    molblock = Chem.MolToMolBlock(mol)
#     print(molblock)
    with open(sdf_res_file,'a') as f:
        f.write(molblock)
        f.write('\n$$$$\n')
```


* ref: https://www.jianshu.com/p/c0df2942d8d1
