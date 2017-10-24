# -*- coding: utf-8 -*-
# 1. black display and text center and bumb
# 2. video and fade in and text center 3 seconds
# 3. fade in and fade out and 3 seconds
# 4. black display and text
# 5. image 4 0.8
# 6. gmarket

import numpy as np
import time
from moviepy.editor import *


#print(TextClip.list('font'))
# 1. black display and text center and bumb
width = 1920 / 4
height = 1080 / 4
step1_text = u'노동계와 정부 간 국정파'
step1_duration = 3;

step2_video_name = 'gmarket.mp4'
step2_text = u'ttttttttt'

step3_video_name = 'auction.mp4'
step3_text = u'auction auction'

step4_text = u'endendendend'

logo_name = 'logo.mp4'

#set black
blackimage = np.zeros([height, width, 3], dtype=np.uint8)
blackimage.fill(0)


step1_text_video = TextClip(step1_text.encode('utf-8'), fontsize=20, color='white', font='NanumBarunGothic-UltraLight')
step1_text_video = step1_text_video.set_duration(step1_duration)
step1_text_video = step1_text_video.set_pos("center")

step1 = ImageClip(blackimage).set_duration(step1_duration)

video = CompositeVideoClip([step1,step1_text_video])

#effect
video = video.fadein(1)




step2_video = VideoFileClip(step2_video_name).subclip(0,5)
step2_video = step2_video.resize(height=height)

step2_text_video = TextClip(step2_text.encode('utf-8'), fontsize=20, color='white', font='NanumBarunGothic-UltraLight')\
    .set_duration(step2_video.duration).set_position(("center","top"))

step2_video = CompositeVideoClip([step2_video, step2_text_video]).fadein(1).fadeout(1)



step3_video = VideoFileClip(step3_video_name).subclip(0,5)
step3_video = step3_video.resize(height=height)

step3_text_video = TextClip(step3_text.encode('utf-8'), fontsize=20, color='white', font='NanumBarunGothic-UltraLight')\
    .set_duration(step2_video.duration).set_position(("center","bottom"))

step3_video = CompositeVideoClip([step3_video, step3_text_video]).fadein(1).fadeout(1)


step4_video = ImageClip(blackimage).set_duration(3)

step4_text_video = TextClip(step4_text.encode('utf-8'), fontsize=20, color='white', font='NanumBarunGothic-UltraLight')\
    .set_duration(3).set_position("center")

step4_video = CompositeVideoClip([step4_video, step4_text_video]).fadein(1).fadeout(1)

step5_video = VideoFileClip(logo_name).resize((width,height))

video = concatenate_videoclips([video, step2_video, step3_video, step4_video, step5_video], method='compose')



datatime = time.strftime("%H%M%S.mp4", time.localtime())
video.write_videofile(datatime, fps=30)



# def textImpression(text, duration, fontsize, fps=30):
#     return [TextClip(step4_text.encode('utf-8'), fontsize=100-fontsize-x*(), color='white', font='NanumBarunGothic-UltraLight') \
#         .set_duration(0.1).set_position("center") for x in range(0,fps)]

#step1_text_video.set_position(("center"))