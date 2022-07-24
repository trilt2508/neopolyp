import os 
import glob
import random
import numpy as np


root = "bkai-igh-neopolyp"
train_names = glob.glob(f"{root}/train/train/*")
val_split_names = np.random.choice(train_names, size=50, replace=False)
os.makedirs(f"{root}/val/val", exist_ok=True)
os.makedirs(f"{root}/val_gt/val_gt", exist_ok=True)

for val_name in val_split_names:
    val_basename = os.path.basename(val_name)
    print(val_basename)
    # os.makedirs("val/val", exist_ok=True)
    # print(os.path.isfile(f"{root}/train/train/{val_basename}"))
    # print(os.path.isfile(f"{root}/train_gt/train_gt/{val_basename}"))
    os.replace(f"{root}/train/train/{val_basename}", f"{root}/val/val/{val_basename}")
    os.replace(f"{root}/train_gt/train_gt/{val_basename}", f"{root}/val_gt/val_gt/{val_basename}")
