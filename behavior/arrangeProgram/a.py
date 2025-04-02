import pandas as pd

def read_first_row_as_list(file_path):
    df = pd.read_excel(file_path)
    return df.columns.tolist()

# 請將 file_path 替換為你的 Excel 文件路徑
file_path = "/Users/477z/Desktop/EmoDNN/behavior/unstandardData.xlsx"
first_row_list = read_first_row_as_list(file_path)

print(first_row_list)
