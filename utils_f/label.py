# AUTOGENERATED! DO NOT EDIT! File to edit: ../label.ipynb.

# %% auto 0
__all__ = ['return_annotation_map', 'get_label_cub2002011']

# %% ../label.ipynb 1
import os
from pathlib import Path

from fastai.vision.data import parent_label

# %% ../label.ipynb 5
def return_annotation_map():
    
    anno_path = Path("D:\AI_Bender\CVsion\IRetrieval_cnn\Data\ImageNet\LOC_synset_mapping.txt")
    
    with open(anno_path, "r") as anno_file:
        strs = anno_file.readlines()
        
    lbl_name_map = {}
    for string in strs:
        str_split = string.split()
        
        lbl = str_split[0]
        name = " ".join(str_split[1:]).split(",")[0]
        lbl_name_map[lbl] = name
        
    return lbl_name_map
    
# With this way of splitting name, there are some repeated names in the original ImageNet dataset.
# Fortunately, there are none in this ImageNet extracted dataset.


def get_label_cub2002011(img_path):

    return parent_label(img_path).split(".")[1]
