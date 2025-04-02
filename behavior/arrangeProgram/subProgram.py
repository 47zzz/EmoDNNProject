
def f(x, y):
    return int((x ** 2 - x) / 2 + y)
#輸入受試者資料
import pandas as pd
# 指定Excel檔案路徑
excel_file_path = '/Users/477z/Desktop/EmoDNN/behavior/unstandardData.xlsx'  # 將 "your_file.xlsx" 替換為實際的檔案路徑


# 使用pandas的read_excel函數讀取Excel檔案
excel_data = pd.read_excel(excel_file_path)

# list
rows_list = excel_data.values.tolist()
print(rows_list)


allRDMs = {}
count = 384


for k in range(35):
    temp = []
    for i in range(count - 1):
        for j in range(i + 1):
            distance = ((rows_list[k*2][i + 1] - rows_list[k*2][j])**2 + (rows_list[k*2 + 1][i + 1] - rows_list[k*2 + 1][j])**2) ** (1/2)#算距離
            temp.append(distance) #轉為原始的資料型態後存入陣列
    allRDMs.update({f"ED{k+1}":temp})
    

'''
    
#print(negRDMs)
'''
RDM = []
for i in range(count - 1):
    for j in range(i + 1):
        distance = ((data.x[i + 1] - data.x[j])**2 + (data.y[i + 1] - data.y[j])**2) ** (1/2)
        RDM.append(correlation_coefficient) #轉為原始的資料型態後存入陣列
RDMs.update({"d1":RDM})



from statistics import correlation

RDMs = {}

d1 = []
d2 = []
d3 = []#三個向度裡面的資料

count = 0
for l in range(0, len(data), 3):
    d1.append(data[l])
    count += 1
for l in range(1, len(data), 3):
    d2.append(data[l])

for l in range(2, len(data), 3):
    d3.append(data[l])

#print(d3[7])
#print(d3[0])

RDM = []
for i in range(count - 1):
    for j in range(i + 1):
        correlation_coefficient = 1 - correlation(d1[i + 1], d1[j])
        RDM.append(correlation_coefficient) #轉為原始的資料型態後存入陣列
RDMs.update({"d1":RDM})

RDM = []
for i in range(count - 1):
    for j in range(i + 1):
        correlation_coefficient = 1 - correlation(d2[i + 1], d2[j])
        RDM.append(correlation_coefficient) #轉為原始的資料型態後存入陣列
RDMs.update({"d2":RDM})

RDM = []
for i in range(count - 1):
    for j in range(i + 1):
        correlation_coefficient = 1 - correlation(d3[i + 1], d3[j])
        RDM.append(correlation_coefficient) #轉為原始的資料型態後存入陣列
RDMs.update({"d3":RDM})

#print(RDMs)
#print(f(7,0))
#print(RDMs.get("d3")[21])
'''
import csv

all_file_path = '/Users/477z/Desktop/EmoDNN/behavior/all/allSubRDMS.csv'


# 清空 CSV 檔案的資料
def clear_csv_file(a):
    with open(a, 'w', newline='') as csvfile:
        csvfile.truncate()  # 使用 truncate() 方法清空檔案
clear_csv_file(all_file_path)

#寫入RDM資訊

import pandas as pd
alldf = pd.DataFrame(allRDMs)

alldf.to_csv(all_file_path, index=False)



#負責檢查順序是否與deep learning那邊相同
import pandas as pd

def read_first_row_as_list(file_path):
    df = pd.read_excel(file_path)
    return df.columns.tolist()

# 請將 file_path 替換為你的 Excel 文件路徑

sub = read_first_row_as_list(excel_file_path)

import os
import torch
from torchvision.io import read_image



def get_image_paths_in_folder(folder_path):
    # 檢查資料夾是否存在
    file_list = sorted(os.listdir(folder_path))
    if not os.path.exists(folder_path):
        print(f"資料夾 '{folder_path}' 不存在")
        return

    # 儲存所有圖片的完整路徑
    image_paths = []

    # 獲取資料夾中的所有文件
    for filename in file_list:
        # 檢查文件是否為圖片
        if filename.endswith(('.jpg', '.jpeg')):
            # 結合資料夾路徑和文件名，得到完整路徑
            
            # 將完整路徑添加到列表中
            image_paths.append(filename)

    return image_paths


# 指定資料夾的路徑
folder_path = '/Users/477z/Desktop/EmoDNN/behavior/neg/neg192'


# 呼叫函式
image_paths = get_image_paths_in_folder(folder_path)
count = 0
substring_to_remove = ".jpg"

picname = []
for name in image_paths:
    picname.append(name.replace(substring_to_remove, ""))

#print(picname)
for i in range(256):
    print(picname[i] == sub[i]) #用來驗證是否排序相同





