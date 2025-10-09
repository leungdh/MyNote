

## 用法
```py
from rdkit.Chem.rdmolops import RDKFingerprint
fp = RDKFingerprint(x)
```

## 参数含义
* mol：要使用的分子。
* minPath：（可选参数）子图中包含的最小键数，默认为1。
* maxPath：（可选参数）子图中包含的最大键数，默认为7。
* fpSize：（可选参数）指纹中的位数，默认为2048。
* nBitsPerHash：（可选参数）每个路径设置的位数，默认为2。如果此值大于1，则每个子图将设置多个比特位。额外的比特位将通过使用原始比特位ID作为随机数生成器的种子，并生成适当数量的随机数来生成。
* useHs：（可选参数）如果分子中有显式的氢原子，则包括涉及氢原子的路径。默认为True。
* tgtDensity：（可选参数）折叠指纹直到达到此最小密度为止。默认为0。如果此值大于零，则指纹将重复折叠直到设置的比特位密度大于或等于此值，或者指纹仅包含minSize比特位。请注意，这意味着生成的指纹大小不一定是您请求（fpSize）的大小。
* minSize：（可选参数）在尝试达到tgtDensity时，折叠指纹的最小大小。默认为128。
* branchedPaths：（可选参数）如果设置为True，则使用分支路径和非分支路径。默认为True。如果为true（默认值），算法将使用子图（即特征可以是分支的）。如果为false，则仅考虑线性路径。
* useBondOrder：（可选参数）如果设置为True，则在路径散列中使用键的顺序。默认为True。如果为true（默认值），则在对子图进行哈希处理时会考虑键的类型，否则将忽略此哈希的组成部分。
* atomInvariants：（可选参数）要在路径散列中使用的原子不变量序列。默认为空。
* fromAtoms：（可选参数）原子索引序列。如果提供，则只使用从这些原子开始的路径/子图。默认为空。
* atomBits：（可选参数）一个空列表。如果提供，则结果将包含一个列表，其中包含每个原子设置的位。默认为空。
* bitInfo：（可选参数）一个空字典。如果提供，则结果将包含一个带有位作为键和相应的键路径作为值的字典。默认为空。

该算法的目的是从输入的分子中生成一个指纹，用于描述分子的结构和特征。指纹是一个二进制位向量，其中每个位表示一种特定的化学子结构或性质。通过调整算法中的参数，可以控制指纹的大小、密度和包含的信息。



## ref
RDKFingerprint介绍：

https://rdkit.org/docs/RDKit_Book.html#additional-information-about-the-fingerprints

https://www.daylight.com/dayhtml/doc/theory/theory.finger.html

函数介绍：
https://www.rdkit.org/docs/source/rdkit.Chem.rdmolops.html#rdkit.Chem.rdmolops.RDKFingerprint

计算全长的rdkitfingerprint： https://greglandrum.github.io/rdkit-blog/posts/2023-01-18-fingerprint-generator-tutorial.html