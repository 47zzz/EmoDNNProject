import os
import torch
from torchvision.io import read_image



def get_image_paths_in_folder(folder_path):
    # 檢查資料夾是否存在
    file_list = sorted(os.listdir(folder_path))
    print(file_list)
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
            full_path = os.path.join(folder_path, filename)
            # 將完整路徑添加到列表中
            image_paths.append(full_path)

    return image_paths


# 指定資料夾的路徑
folder_path = '/Users/477z/Desktop/EmoDNN/behavior/neuv2/neu192'


# 呼叫函式
image_paths = get_image_paths_in_folder(folder_path)




#儲存圖片資料
imgs = []

# 將圖片的tensor轉入 imgs
for path in image_paths:
    print(path)
    imgs.append(read_image(path))

from torchvision.models import vgg16, VGG16_Weights

#以下為初始化model
# Step 1: Initialize model with the best available weights
weights = VGG16_Weights.DEFAULT
model = vgg16(weights=weights)
model.eval()

#print(model)
# Step 2: Initialize the inference transforms
preprocess = weights.transforms(antialias=True)

# Step 3: Apply inference preprocessing transforms
batchs = [] #儲存處理過後的imgs
count = 0
for img in imgs:
    batchs.append(preprocess(img).unsqueeze(0))
    count += 1
# Step 4: Use the model and print the predicted category

'''
predictions = []
for batch in batchs:
    predictions.append(model(batch).squeeze(0).softmax(0))

for prediction in predictions:
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    print(f"{category_name}: {100 * score:.1f}%")
'''

import torch.nn as nn
from torch_intermediate_layer_getter import IntermediateLayerGetter as MidGetter

def f(x, y):
    return int((x ** 2 - x) / 2 + y)

#以下為取出各層並做相關
if __name__ == '__main__':

    return_layers = {
        'features.1':'conv1',
        'features.4':'conv2',
        'features.6':'conv3',
        'features.9':'conv4',
        'features.11':'conv5',
        'features.13':'conv6',
        'features.16':'conv7',
        'features.18':'conv8',
        'features.20':'conv9',
        'features.23':'conv10',
        'features.25':'conv11',
        'features.27':'conv12',
        'features.30':'conv13',
        'classifier.1':'fc6',
        'classifier.4':'fc7'
    }
    mid_getter = MidGetter(model, return_layers=return_layers, keep_output=False)##取
    
    RDMs = {}
    
    for layer in return_layers.values(): ##一層一層取
        outputs = []
        for batch in batchs: #一張照片一張照片進去，將結果放入outputs裡
            mid_outputs, model_output = mid_getter(batch)
            outputs.append(mid_outputs[layer])
        
        reOutputs = []# outputs裏面每一個output都是一張照片的DNN取層結果
        for output in outputs:#由於每個output結果維度不易計算相關，將其轉換
            resolution = output.numel()
            reOutputs.append(output.reshape(resolution)) #拉呈直線
        print(resolution)
        RDM = []
        #直接計算相關
        for i in range(count - 1):
            for j in range(i + 1):
                    stack = torch.stack((reOutputs[i + 1], reOutputs[j]), dim = 0)#兩兩照片疊一起 以做相關
                    correlation = 1 - torch.corrcoef(stack) #算 1 - 相關 = dissimilarity
                    RDM.append(correlation[0, 1].item()) #轉為原始的資料型態後存入陣列
        RDMs.update({layer:RDM})
    
    #print(RDMs.get('conv5')[f(3,2)])

#輸出結果成csv檔

import csv

csv_file_path = '/Users/477z/Desktop/EmoDNN/behavior/neuv2/neuRDMS.csv'

# 清空 CSV 檔案的資料
def clear_csv_file():
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvfile.truncate()  # 使用 truncate() 方法清空檔案
clear_csv_file()
#寫入RDM資訊

import pandas as pd
df = pd.DataFrame(RDMs)
df.to_csv(csv_file_path, index=False)


#print(RDMs)





