
### 用法
```py
smiless = [Chem.MolToSmiles(mol) for mol in database]

mol_smi = Chem.MolToSmiles(mol, isomericSmiles = True, canonical= True)

```
* 当前版本使用默认参数可以转化带有立体化学信息的SMILES
* 需要注意的是这样转化的坐标是无法控制的，即如果再用这个mol生成图片，图片可能是“歪”的
* https://zhuanlan.zhihu.com/p/392213951
### 参数
* Mol: 分子对象，表示要转换的分子。
* isomericSmiles: （可选）是否包含立体化学信息，默认为True。
* kekuleSmiles: （可选）是否使用Kekule式（非芳香键）的SMILES，默认为False。
* rootedAtAtom: （可选）如果为非负数，则强制SMILES从特定原子开始，默认为-1。
* canonical: （可选）如果为False，则不尝试对分子进行规范化，默认为True。
* allBondsExplicit: （可选）如果为True，则在输出的SMILES中显示所有键的键阶，默认为False。
* allHsExplicit: （可选）如果为True，则在输出的SMILES中显示所有氢原子数，默认为False。


### 源码
```py
def MolToSmiles(Mol, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    MolToSmiles( (Mol)mol [, (bool)isomericSmiles=True [, (bool)kekuleSmiles=False [, (int)rootedAtAtom=-1 [, (bool)canonical=True [, (bool)allBondsExplicit=False [, (bool)allHsExplicit=False [, (bool)doRandom=False]]]]]]]) -> str :
        Returns the canonical SMILES string for a molecule
          ARGUMENTS:
        
            - mol: the molecule
            - isomericSmiles: (optional) include information about stereochemistry in
              the SMILES.  Defaults to true.
            - kekuleSmiles: (optional) use the Kekule form (no aromatic bonds) in
              the SMILES.  Defaults to false.
            - rootedAtAtom: (optional) if non-negative, this forces the SMILES 
              to start at a particular atom. Defaults to -1.
            - canonical: (optional) if false no attempt will be made to canonicalize
              the molecule. Defaults to true.
            - allBondsExplicit: (optional) if true, all bond orders will be explicitly indicated
              in the output SMILES. Defaults to false.
            - allHsExplicit: (optional) if true, all H counts will be explicitly indicated
              in the output SMILES. Defaults to false.
        
          RETURNS:
        
            a string
        
        
    
        C++ signature :
            std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > MolToSmiles(RDKit::ROMol [,bool=True [,bool=False [,int=-1 [,bool=True [,bool=False [,bool=False [,bool=False]]]]]]])
    """
    pass
```