
* example
```py
plot.scatter(x1, x2, colormap='jet', alpha = 0.3)
```
* 参数
  * colormap: 可选'Blues', 'jet', ...
    * https://blog.csdn.net/qq_37851620/article/details/100642566
  * c：设定特定颜色
  * vmin, vmax: colorbar的区间

* 完整示例：
```py
figure = plt.figure(figsize=(6,5), dpi =300)

colors = ['#686789','#AB545A','#BEB1A8']

l1 = plt.scatter(X_embedded1[:,0],X_embedded1[:,1],c = colors[0],alpha= 0.3)
l2 = plt.scatter(X_embedded2[:,0],X_embedded2[:,1],c = colors[1],alpha= 0.3)
l3 = plt.scatter(X_embedded3[:,0],X_embedded3[:,1],c = colors[2],alpha= 0.3)

plt.legend(handles=[l1,l2,l3],labels = ['6-','6-7','7+'], loc = 'lower left')

plt.title('RDKFP2048',fontsize=12)
plt.savefig('RDKFP2048.png')
plt.show()

```

* ref
  * https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html