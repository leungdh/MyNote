Save in different batches 分批保存
```py
chunk_size = len(df) // 10

# 拆分并保存
for i in range(10):
    start_row = i * chunk_size
    end_row = (i + 1) * chunk_size if i < 9 else len(df)  # 确保最后一个分片包含所有剩余行
    chunk_df = df.iloc[start_row:end_row]
    file_name = f'N2pb.0709.{i+1}.xlsx'
    chunk_df.to_excel('/data3/liangdh/project/alnp/n2pb_temp/'+file_name, index=False)
    print(f'Saved: {file_name}')

```

```py
num_rows = len(df_join)
chunk_size = num_rows // 10

# 分割并保存
for i in range(10):
    start_row = i * chunk_size
    if i < 9:
        end_row = (i + 1) * chunk_size
    else:
        end_row = num_rows  # 确保最后一份包含所有剩余的行

    chunk_df = df_join.iloc[start_row:end_row]

    # 保存文件，例如保存为 CSV 文件
    chunk_df.to_excel(f'huanji_smallMW_AImols_{i+1}.xlsx', index=False)

```
