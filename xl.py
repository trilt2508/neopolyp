import cv2
import numpy as np
img = cv2.imread("./anh1.jpeg")
print(img.shape)
A = []
img_ = np.array(img)
for i in range(0,img_.shape[0]):
    for j in range(0,img_.shape[1]):
        # if list(img_[i][j]) not in A:
        #     A.append(list(img_[i][j]))
        img_[i][j] = np.array([89, 190, 92])
print(A)

cv2.imshow("image", img_)
cv2.waitKey(0)