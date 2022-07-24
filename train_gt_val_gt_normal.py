import imp
import os
import cv2
import numpy as np
train_gt_dir = ".\\bkai-igh-neopolyp\\train_gt\\train_gt"
count = 0
for pth in os.listdir(train_gt_dir):
    if count < 900 or count >= 1000:
        count += 1
        continue
    print(count)
    count += 1
    img = cv2.imread(train_gt_dir+"\\"+pth)
    print(train_gt_dir+"/"+pth)
    img = cv2.resize(img, [1280,1024], cv2.INTER_LINEAR)
    print(img.shape)
    for i in range(0,1024):
        for j in range(0,1280):
            if img[i][j][1] > 127:
                img[i][j] = np.array([0,255,0])
            elif img[i][j][2] > 127:
                img[i][j] = np.array([0,0,255])
            else:
                img[i][j] = np.array([0,0,0])
    # A = []
    # cv2.imshow("img",img)
    # for i in range(0,1024):
    #     for j in range(0,1280):
    #         if list(img[i][j]) not in A:
    #             A.append(list(img[i][j]))
    # print(A)
    # cv2.waitKey(0)
    # break
    cv2.imwrite(f".\\bkai-igh-neopolyp\\train_gt\\image{count}.png", img)

# val_gt_dir = ".\\kaggle\\input\\bkai-neopolyp\\bkai-igh-neopolyp\\val_gt\\val_gt"
# count = 0
# for pth in os.listdir(val_gt_dir):
#     img = cv2.imread(val_gt_dir+"\\"+pth)
#     print(val_gt_dir+"/"+pth)
#     img = cv2.resize(img, [1280,1024], cv2.INTER_LINEAR)
#     print(img.shape)
#     for i in range(0,1024):
#         for j in range(0,1280):
#             if img[i][j][1] > 127:
#                 img[i][j] = np.array([0,255,0])
#             elif img[i][j][2] > 127:
#                 img[i][j] = np.array([0,0,255])
#             else:
#                 img[i][j] = np.array([0,0,0])
#     cv2.imwrite(f".\\kaggle\\input\\bkai-neopolyp\\bkai-igh-neopolyp\\val_gt\\image{count}.jpg", img)
#     count += 1