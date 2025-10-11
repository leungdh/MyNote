Read multiple excel and combine 批量读取并合并df
```py
import os
import pandas as pd
import glob

# 设置文件夹路径
folder_path = '/mypath/'  # 替换为实际的文件夹路径

# 使用glob获取所有符合条件的文件路径
file_pattern = os.path.join(folder_path, 'filename.*.feas.xlsx')
file_list = glob.glob(file_pattern)

# 初始化一个空的DataFrame
combined_df = pd.DataFrame()

# 逐个读取文件并拼接
for file in file_list:
    df = pd.read_excel(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 打印或保存最终的DataFrame
print(combined_df)


```

