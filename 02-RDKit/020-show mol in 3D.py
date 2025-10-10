show mol in 3D, 分子3D显示
```py
import py3Dmol

def molecule_to_3d(mol, viz_flag=False):
    mol = AllChem.AddHs(mol, addCoords=True)
    AllChem.EmbedMolecule(mol, randomSeed=1, useRandomCoords=True)
    AllChem.MMFFOptimizeMolecule(mol)
    if viz_flag:
        view = py3Dmol.view(
            data=Chem.MolToMolBlock(mol),  # Convert the RDKit molecule for py3Dmol
            style={"stick": {'colorscheme':'orangeCarbon'}} #, "sphere": {"scale": 0.3}}
            )
        view.zoomTo()
        display(view)
    return mol

```
