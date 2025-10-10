

* ref: https://blog.csdn.net/fengdu78/article/details/107888652

```py
plt.subplot(2,2,1) # plt.subplot(221)

plt.subplot(2,2,2)

plt.subplot(2,2,3)

plt.subplot(2,2,4)
```

```py
plt.subplot(2,2,1)
plt.plot(x,x*x)

plt.subplot(2,2,2)
plt.scatter(np.arange(0,10), np.random.rand(10))

plt.subplot(2,2,3)
...

plt.subplot(2,2,4)
...
```