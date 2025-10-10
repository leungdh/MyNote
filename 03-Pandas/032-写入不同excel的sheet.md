```py
# 创建 ExcelWriter 对象
with pd.ExcelWriter('output.xlsx') as writer:
    # 将 DataFrame 写入不同的 sheet 并命名
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)    
```