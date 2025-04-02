
from PIL import Image
#import matplotlib.pyplot as plt
import os
import torch
from torchvision.io import read_image
from torchvision.utils import make_grid
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as T
import torch
import torch.nn as nn
from torchvision.utils import make_grid
from torchvision.utils import save_image
from IPython.display import Image
import matplotlib.pyplot as plt
import numpy as np
import random


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
folder_path = '/Users/477z/Desktop/EmoDNN/behavior/all/allImage'


# 呼叫函式
image_paths = get_image_paths_in_folder(folder_path)




#儲存圖片資料
imgs = []

# 將圖片的tensor轉入 imgs
for path in image_paths:
    print(path)
    imgs.append(read_image("/Users/477z/Desktop/EmoDNN/behavior/all/allImage/neu_188.jpg"))

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
def show_images(images, nmax=64):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks([]); ax.set_yticks([])
    ax.imshow(make_grid((images.detach()[:nmax]), nrow=8).permute(1, 2, 0))
def show_batch(dl, nmax=64):
    for images in dl:
        show_images(images, nmax)
        break

for img in imgs:

    transformed_image = preprocess(img)
    
#    fig, ax = plt.subplots(figsize=(8, 8))
#    fig, ax = plt.plot()
#    ax.set_xticks([]); ax.set_yticks([])
    plt.imsave('test.png', transformed_image.permute(1, 2, 0))
#    fig.figsave('test.png')
#    plt.colse()
    break
#    count += 1
#    output_path = 'transformed_image.jpg'
#    transformed_image_pil = show_images(transformed_image)
#    transformed_image_pil.savefig(output_path)

    # 使用操作系統的圖片查看器打開轉換後的圖片
