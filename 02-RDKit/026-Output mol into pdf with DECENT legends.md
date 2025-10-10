Output mol into pdf with DECENT legends 画图打印legend并保存pdf

```py
from rdkit.Chem import Draw

img = Draw.MolsToGridImage([Chem.MolFromSmiles(smi)for smi in df['Whole.SMILES']],
                        maxMols = len(df),molsPerRow = 5, subImgSize = (350,350),returnPNG=False, useSVG=False,
                          legends = ["MolID: {}, clogP: {:.2f}\n MW: {:.2f}, ApKa.prob: {:.2f}".
                                format(row["MolID"],row["Whole.clogp"],row["Whole.MW"],
                                       (row["Whole.apka.prob.v11-44"]+row["Whole.apka.prob.v11-14"])/2)
                                for index, row in df.iterrows()])
display(img)  
img.save('myfig.png')  

```
