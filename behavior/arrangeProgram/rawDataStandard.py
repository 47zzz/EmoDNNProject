import pandas as pd
from scipy.stats import zscore

def convert_to_z_score(input_excel, output_excel):
    # 读取Excel文件
    df = pd.read_excel(input_excel)

    # 计算每一行的Z分数
    z_score_df = df.apply(zscore, axis=0)

    # 保存转换后的数据框到新的Excel文件
    z_score_df.to_excel(output_excel, index=False)

# 替换为你的输入和输出Excel文件路径
input_excel_file = '/Users/477z/Desktop/EmoDNN/behavior/unstandardData.xlsx'

output_excel_file = '/Users/477z/Desktop/EmoDNN/behavior/normalizedData.xlsx'

convert_to_z_score(input_excel_file, output_excel_file)
def calculate_row_mean(input_excel):
    # 读取Excel文件
    df = pd.read_excel(input_excel)

    # 计算每一行的平均值
    row_means = df.mean(axis=1)

    # 打印每一行的平均值
    for idx, mean in enumerate(row_means):
        print(f'Row {idx + 1} Mean: {mean}')
calculate_row_mean(output_excel_file)
