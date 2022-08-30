"""
how to use 
    Drop the image you want to edit into the program file

1 : The color after transparency can be changed from RGB
2 : Only supports white background for black text

@TakenoSite
"""


import cv2
import numpy as np
import sys


input_path  = sys.argv

class Trace(object):
    def __init__(self,path) -> None:
        self.img_load = cv2.imread(path)
        self.img_thresh()
        self.add_alpha_channel()

        super().__init__()
    
    def img_thresh(self):
        openImg = self.img_load
        threshold = 210  # If there is a lot of roughness, lower it. 
        
        ret,img_thresh = cv2.threshold(openImg,threshold,255,cv2.THRESH_BINARY)
        
        self.img_thresh = img_thresh

    def add_alpha_channel(self):
        b,g,r = cv2.split(self.img_thresh)
        alpha_channel = np.ones(b.shape,dtype=b.dtype)*255
        alpha_channel[:,:int(b.shape[0])] = 255
        img_rgb = cv2.merge((b,r,g,alpha_channel))

        img_rgb[:,:,3] = np.where(np.all(img_rgb == 255,axis=-1),0,255)

        
        #Color specification after transparency
        
        R = 255
        G = 255
        B = 255
        
        #######

        img_rgb[:,:,0] = np.where(np.all(img_rgb == 255,axis=-1),0,B)
        img_rgb[:,:,1] = np.where(np.all(img_rgb == 255,axis=-1),0,G)
        img_rgb[:,:,2] = np.where(np.all(img_rgb == 255,axis=-1),0,R)
        
        FILENAME = "./OutPut.png"
        cv2.imwrite(FILENAME,img_rgb)

if __name__ == "__main__":
    Trace(input_path[1])
