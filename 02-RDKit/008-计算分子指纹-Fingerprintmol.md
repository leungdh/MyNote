# 计算分子指纹-FingerprintMol
### 建议直接调用分子指纹函数RDKFingerprint，而不是FingerprintMol。因为如果生成的FP密度小于0.3（*），FingerprintMol会将FP折叠直到FP密度大于0.3.这会使得FP的维度不可控，需要FP生成完才知道FP的维度是多少，而不是自己设定的值，如默认2048.
[RDKFingerprint](./计算分子指纹%20函数RDKFingerprint.md)

## 用法介绍
```py
from rdkit import Chem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols

#算分子指纹
#FingerprintMol默认用的分子指纹是Chem.RDKFingerprint
#database是一个列表，放了各个分子，type: rdkit.Chem.rdchem.Mol
fps = [FingerprintMols.FingerprintMol(mol) for mol in database]
```

## 和RDKFingerprint的区别
* FingerprintMol默认调用的分子指纹算法是RDKFingerprint
* 但FingerprintMol会自动将生成的分子指纹不断折叠，使得分子指纹密度大于默认值（fpArgs['tgtDensity']=0.3，来源待考究），才会停下。除非分子指纹已经折叠到默认的最小值（fpArgs['minSize']=128，待考究）
### 相关源码
```py
def FingerprintMol(mol, fingerprinter=Chem.RDKFingerprint, **fpArgs):
  if not fpArgs:
    fpArgs = FingerprinterDetails().__dict__

  if fingerprinter != Chem.RDKFingerprint:
    fp = fingerprinter(mol, **fpArgs)
    return FoldFingerprintToTargetDensity(fp, **fpArgs)

  return fingerprinter(mol, fpArgs['minPath'], fpArgs['maxPath'], fpArgs['fpSize'],
                       fpArgs['bitsPerHash'], fpArgs['useHs'], fpArgs['tgtDensity'],
                       fpArgs['minSize'])

def FoldFingerprintToTargetDensity(fp, **fpArgs):
  nOn = fp.GetNumOnBits()
  nTot = fp.GetNumBits()
  while float(nOn) / nTot < fpArgs['tgtDensity']:
    if nTot / 2 > fpArgs['minSize']:
      fp = DataStructs.FoldFingerprint(fp, 2)
      nOn = fp.GetNumOnBits()
      nTot = fp.GetNumBits()
    else:
      break
  return fp

```
