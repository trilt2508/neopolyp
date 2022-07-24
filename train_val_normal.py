import os
import cv2
train_dir = ".\\bkai-igh-neopolyp\\train\\train"
count = 0
for pth in os.listdir(train_dir):
    count += 1
    img = cv2.imread(train_dir+"\\"+pth)
    print(train_dir+"/"+pth)
    img = cv2.resize(img, [1280,1024], cv2.INTER_LINEAR)
    print(img.shape)
    cv2.imwrite(f".\\bkai-igh-neopolyp\\train\\image{count}.png", img)
# val_dir = ".\\kaggle\\input\\bkai-neopolyp\\bkai-igh-neopolyp\\val\\val"
# count = 0
# for pth in os.listdir(val_dir):
#     img = cv2.imread(val_dir+"\\"+pth)
#     print(val_dir+"/"+pth)
#     img = cv2.resize(img, [1280,1024], cv2.INTER_LINEAR)
#     print(img.shape)
#     cv2.imwrite(f".\\kaggle\\input\\bkai-neopolyp\\bkai-igh-neopolyp\\val\\image{count}.jpg", img)
#     count += 1