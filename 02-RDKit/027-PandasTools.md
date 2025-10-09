```py
from rdkit.Chem import PandasTools
PandasTools.RenderImagesInAllDataFrames()
PandasTools.AddMoleculeColumnToFrame(df_feas_refine, smilesCol="SMILES1", molCol="Lipid1.Mol")
PandasTools.AddMoleculeColumnToFrame(df_feas_refine, smilesCol="SMILES2", molCol="Lipid2.Mol")
PandasTools.SaveXlsxFromFrame(frame, 'huanji.reverse.xlsx', molCol=["Lipid1.Mol", "Lipid2.Mol"])
```