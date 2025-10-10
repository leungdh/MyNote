```py
plt.figure(figsize=(5, 4),dpi=100)
plt.scatter(df[fea], df[PROP],alpha=0.4)
plt.title("K-Series Features")
labels = df['Compound_ID'].tolist()
plt.annotate(f"R = {r:.2f}\np-value = {p:.2e}",xy=(-0.05, 1.05), xycoords='axes fraction')
for i, label in enumerate(labels):
    plt.annotate(label, (df[fea][i],df[PROP][i]))
```