# 设置图片大小和分辨率

## 设置图片大小

```py
figure = plt.figure(figsize=(6,5))
```

* figsize 参数用于设置图形的尺寸，它接受一个包含两个值的元组 (width, height)。其中 width 是图形的宽度，height 是图形的高度，单位为英寸（inch）。
* 设置6英寸*5英寸的图片，适合搭配xlabel，ylabel的fontsize是15左右，xticks，yticks的fontsize是12左右
* 如果不改变fontsize，但增大figsize，那么图片里的字会显得小很多
* 一般作图figsize长宽根据需要设置在4-8就挺合适的了

## 设置图片分辨率
### 在创建的时候设置
```py
figure = plt.figure(figsize=(6,5), dpi = 300)
```
### 在保存的时候设置
```py
plt.savefig('figname.png',dpi = 300)
```
* dpi 表示每英寸点数（dots per inch），它决定了输出图片的分辨率。具体而言，dpi 值越大，生成的图片分辨率越高，图像细节越清晰。
* 通常情况下，可以将 dpi 设置为一个较高的值（如 300 或 600）以获得高分辨率的输出图片。


### 总结起来，figsize 控制图形在屏幕上显示的尺寸，而 dpi 控制保存的图片的分辨率。它们可以相互配合使用，以获得预期的图形效果和输出质量。