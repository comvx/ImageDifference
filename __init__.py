import os
import numpy as np
import cv2 
import sys
import tqdm

from Data import *
from Process import *
from PIL import Image, ImageChops
from multiprocessing.pool import ThreadPool
from matplotlib import cm

class InitData:
    def __init__(self, files, mode):
        self.mode = mode
        self.files = files
    def get_handler(self):
        pass
    def get_images_data(self):
        output = list()
        bar = tqdm.tqdm(total=len(self.files))

        for index in range(len(self.files)):
            """init handlers"""
            image = None
            img1 = None
            img2 = None
            file = self.files[index]
            if(self.mode == "-f"):
                image = Image.open(file)
                img1 = Image.open(self.files[index-1])
                img2 = Image.open(self.files[index])
            elif(self.mode == "-m"):
                image = file
                img1 = self.files[index-1]
                img2 = self.files[index]
            image_data = image.load()
            xWidth, yHeight = image.size
            totalSize = xWidth * yHeight


            """rgb/wb"""
            rColor = 0.0
            rWcolor = 0.0
            gColor = 0.0
            gWcolor = 0.0
            bColor = 0.0
            bWcolor = 0.0

            count = 0

            for x in range(xWidth):
                for y in range(yHeight):
                    count += 1
                    rgb = str(image_data[x,y])
                    rgb = rgb.replace("(", "").replace(")", "").replace(" ", "")
                    rgb = rgb.split(",")
                    rColor += int(rgb[0])
                    rWcolor += int(rgb[0]) / 255
                    gColor += int(rgb[1])
                    gWcolor += int(rgb[1]) / 255
                    bColor += int(rgb[2])
                    bWcolor += int(rgb[2]) / 255
            rColor /= totalSize
            gColor /= totalSize
            bColor /= totalSize
            rWcolor /= totalSize
            gWcolor /= totalSize
            bWcolor /= totalSize
            """motion data"""
            diff = 0
            rgb_data = None
            wb_data = None
            if index > 0:
                tmp = ImageChops.difference(img1, img2)
                w,h = tmp.size
                a = np.array(tmp.convert('RGB')).reshape((w*h,3))
                h,e = np.histogramdd(a, bins=(16,)*3, range=((0,256),)*3)
                prob = h/np.sum(h) # normalize
                prob = prob[prob>0] # remove zeros
                diff = -np.sum(prob*np.log2(prob))

                #passed_rgb = output[len(output)-2].get_rgb()
                #passed_wb = output[len(output)-2].get_wb()
                #diff_rgb = (passed_rgb[0] - rColor) + (passed_rgb[1] - gColor) + (passed_rgb[2] - bColor)
                #diff_wb = (passed_wb[0] - rWcolor) + (passed_wb[1] - gWcolor) + (passed_wb[2] - bWcolor)

                rgb_data = [rColor, gColor, bColor, (rColor+gColor+bColor)/3]
                wb_data = [rWcolor, gWcolor, bWcolor, (rWcolor+gWcolor+bWcolor)/3]
            else:
                rgb_data = [rColor, gColor, bColor, 0]
                wb_data = [rWcolor, gWcolor, bWcolor, 0]

            output.append(imageData(rgb_data, wb_data, diff, index))
            bar.update(1)
        return output

def files(path):
    tmp = os.listdir(path)
    for index in range(len(tmp)):
        tmp[index] = path + tmp[index]
    return tmp

def get_frames(path):
    frames = list()
    cam = cv2.VideoCapture(path)
    length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    count = 0
    bar = tqdm.tqdm(total=length)
    while(True):
        ret, frame = cam.read()
        if(ret):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if(genData.ori_size == (0,0)):
                genData.ori_size = ((img.size)[0] , (img.size)[1])
                
            #img.thumbnail((200,200), Image.ANTIALIAS)
            frames.append(img)
            #img.save("C:/Users/maxol/OneDrive/Desktop/ImageDifference/data/" + str(count) + ".png")
            bar.update(1)
            count+=1
        else:
            break
    bar.close()
    return frames

if __name__ == '__main__':
    args = sys.argv

    if(args[1] == "-f"):
        initData = InitData(files("C:/Users/maxol/OneDrive/Desktop/ImageDifference/data/"), "-f") # last '/' is important
        data = initData.get_images_data()
        print(data[2].get_rgb())
        print(data[2].get_wb())
        print(data[2].get_diff())
    elif(args[1] == "-m"):
        procs = ThreadPool(processes=2)
        frames = get_frames("E:/Downloads/testvideo.mp4")
        initData = InitData(frames, "-m")
        #frames = None
        print(genData.ori_size)
        video_data = initData.get_images_data()

        processing = defPoints(video_data)
        output = processing.proc()


        o = list()
        for i in range(len(output)):
            if(output[i].get_point()):
               o.append(str(i))
               img = frames[i]
               img.thumbnail(genData.ori_size, Image.ANTIALIAS)
               #img = img.resize(genData.ori_size)
               img.save("C:/Users/maxol/OneDrive/Desktop/ImageDifference/data/" + str(i+100) + ".png")
        print(o)
