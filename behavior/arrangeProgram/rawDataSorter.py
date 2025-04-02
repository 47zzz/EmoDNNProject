import pandas as pd

# 讀取CSV檔
'''
for i in range(1, 36):  # 从ED1到ED35
    csv_filename = f'/Users/477z/Desktop/EmoDNN/behavior/RAWratingData/ED{i}.csv'  # 构造CSV文件名
    df = pd.read_csv(csv_filename)

    # 按照row的名稱排序

    df_sorted = df.sort_values(by='stimulus_filename')

    # 儲存排序後的CSV檔
    df_sorted.to_csv(csv_filename, index=False)
'''
csv_filename = f'/Users/477z/Desktop/EmoDNN/behavior/stimuli_list.csv'  # 构造CSV文件名
df = pd.read_csv(csv_filename)

# 按照row的名稱排序

df_sorted = df.sort_values(by='0')

# 儲存排序後的CSV檔
df_sorted.to_csv(csv_filename, index=False)
