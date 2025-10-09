
# Atom Pairs
```py
from rdkit import Chem
from rdkit.Chem.AtomPairs import Pairs

fps = [Pairs.GetAtomPairFingerprint(x) for x in all_sdf[:1]]
print('BitString\'s Length:', fps[0].GetLength())
print('GetNonzeroElements: \n', fps[0].GetNonzeroElements())
print('Number of NonzeroElements: \n', len(fps[0].GetNonzeroElements()))

```
out:
```
BitString's Length: 8388608
GetNonzeroElements: 
 {541754: 1, 541755: 1, 558113: 3,1424: 1, 1722474: 1, [此处省略许多个dict元素]1723437: 1, 1723458: 1, 1723466: 1, 1723467: 1} 
Number of NonzeroElements: 
 292
```
* 一个分子算出来的atom pairs是一个很长的字典（如本例中有8388608个bit位），里面很多位会是非空值。本例只有292个是非空bit位。
* `GetNonzeroElements()`:获取非空位，格式是字典。
* `GetLength()`:计算ap有多长。

### 函数的具体参数和功能说明如下：

* Mol：一个分子对象，表示要计算指纹的分子。
* minLength（可选）：一个整数，表示原子对的最小长度，默认为1。
* maxLength（可选）：一个整数，表示原子对的最大长度，默认为30。
* fromAtoms（可选）：一个 AtomPairsParameters 对象，表示参与原子对的原子，默认为0。
* ignoreAtoms（可选）：一个 AtomPairsParameters 对象，表示忽略的原子，默认为0。
* atomInvariants（可选）：一个 AtomPairsParameters 对象，表示原子不变量，默认为0。
* includeChirality（可选）：一个布尔值，表示是否考虑立体化学信息，默认为False。
* use2D（可选）：一个布尔值，表示是否使用二维结构，默认为True。
* confId（可选）：一个整数，表示要使用的构象的 ID，默认为-1。
#### 该函数的返回值是一个 IntSparseIntVect 对象，表示计算得到的原子对指纹。

#### ref
* rdkit: https://www.rdkit.org/docs/source/rdkit.Chem.AtomPairs.Pairs.html
* 