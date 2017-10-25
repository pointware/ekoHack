# -*- coding: utf-8 -*-
import numpy as np
import time
from moviepy.editor import *
width = 1920 / 4
height = 1080 / 4

#set black
blackimage = np.zeros([height, width, 3], dtype=np.uint8)
blackimage.fill(0)

step1_text = u'asdfasdfasdfasdfasdfasdfasdf'

def impress(text, size, enduration = 2,maxsize = 120):
    gap = maxsize - size / 30

    clip = [
        TextClip(text.encode('utf-8'), fontsize=maxsize - size - x * 3, color='white', font='NanumBarunGothic-UltraLight').set_duration(0.01).set_pos("center").set_start(0.01*x)
        for x in range(0,30)
    ]
    clip.append(TextClip(text.encode('utf-8'), fontsize=size, color='white', font='NanumBarunGothic-UltraLight').set_pos("center").set_start(clip[-1].end).set_duration(enduration - clip[-1].end))
    return clip

arr = impress(step1_text, 20)
step1 = ImageClip(blackimage).set_duration(3)
video = CompositeVideoClip([step1]+arr)

datatime = time.strftime("%H%M%S.mp4", time.localtime())
video.write_videofile(datatime, fps=30)