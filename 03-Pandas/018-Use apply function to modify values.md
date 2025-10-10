Use apply function to modify values 
用apply修改dataframe的值
```py
def normalize_value(x):
    return x / 100 if x > 1 else x

# Apply the function to the column
df['values'] = df['values'].apply(normalize_value)

```
