
```py
temp = pd.DataFrame(shap_value.values)
col_mean = temp.mean()
row_mean = temp.mean(axis = 1)
```

```py
df_temp_mtd.groupby(['CustomField.Animal Dose','CustomField.Cytokine.Sampling.Timepoint','CustomField.Compound_ID','CustomField.AB_Code'])['CustomField.IL-6/PBS'].mean().reset_index(name='CustomField.IL-6/PBS')
```