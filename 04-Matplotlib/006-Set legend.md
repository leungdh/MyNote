
```py
plt.legend(handles = [l1,l2,l3], labels = [1,2,3], loc = 'lower left')
```

* 完整示例：
```py
figure = plt.figure(figsize=(6,5), dpi =300)

colors = ['#686789','#AB545A','#BEB1A8']

l1 = plt.scatter(X_embedded1[:,0],X_embedded1[:,1],c = colors[0],alpha= 0.3)
l2 = plt.scatter(X_embedded2[:,0],X_embedded2[:,1],c = colors[1],alpha= 0.3)
l3 = plt.scatter(X_embedded3[:,0],X_embedded3[:,1],c = colors[2],alpha= 0.3)

plt.legend(title = 'pka', handles=[l1,l2,l3],labels = ['6-','6-7','7+'], loc = 'lower left')

plt.title('RDKFP2048',fontsize=12)
plt.savefig('RDKFP2048.png')
plt.show()

```
* ref: 
  * https://zhuanlan.zhihu.com/p/41781440
  * https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html