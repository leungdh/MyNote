```py
from matplotlib import pyplot as plt
plt.style.use("seaborn-v0_8")
figure = plt.figure(figsize=(6,5))

pd.Series(ori_similist).plot(kind = 'kde',label = 'InHouse') 
pd.Series(genmol_similist).plot(kind = 'kde',label = 'GenMols') 
pd.Series(agile_similist).plot(kind = 'kde',label = 'AGILE') 

plt.xlim(0,1.1)
plt.legend()
plt.savefig('/home/liangdh/pythonproject/png/density_inhouse_genmols_agile_x0-1.png')

```