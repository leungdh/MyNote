```py
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

X_embedded = TSNE(n_components=2, learning_rate='auto', init='random', random_state=1).fit_transform(X)

# plot
plt.style.use('seaborn-v0_8')
figure = plt.figure(figsize=(6,5), dpi =150)
colors = ["lightskyblue", "salmon"]

l1 = plt.scatter(X_embedded[:20000,0],X_embedded[:20000,1], color = colors[0], alpha= 0.2)
l2 = plt.scatter(X_embedded[20000:21434,0],X_embedded[20000:21434,1], color = colors[1],alpha= 0.3)

plt.legend(handles=[l1,l2],labels = ['GenMols','InHouse'], loc = 'lower right')
plt.xlim(-87, 110)
plt.ylim(-100, 100)
figtitle = 'Chemical Space'
plt.title(figtitle,fontsize=12)
plt.savefig(r'/home/liangdh/pythonproject/png/tsne_genmols2w_inhouse_21434_color2.png')

```