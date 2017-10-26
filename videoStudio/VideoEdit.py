from moviepy.editor import *
import numpy as np
from moviepy.video.tools.segmenting import findObjects
from moviepy.video.tools.drawing import circle


class VideoTemplate:
    step1_duration = 3
    step3_duration = 3
    step4_duration = 3
    step5_duration = 3
    font = 'Noto-Sans-Mono-CJK-KR-Bold'
    screen = (720, 360)
    fps = 25
    logovideo = 'videoStudio/media/logo3.mp4'

    step1_audio = 'videoStudio/media/startbg.mp3'
    step2_audio = ''
    step3_audio = ''
    step4_audio = 'videoStudio/media/step4-bg.mp3'
    step5_audio = ''

    def CountDown(self, text, fps=20):
        maxsize = 1200
        gap = maxsize / (fps * 2)
        duration = 0.01
        clips = []
        for y in text:
            for x in range(1, fps * 2 + 1):
                clips.append(TextClip(y.encode('utf-8'), size=self.screen, fontsize=maxsize - x * gap, color='white',
                                      font=self.font).set_duration(duration).set_pos("center").set_start(duration * x))

        return concatenate_videoclips(clips, method='compose')

    def impress(self, text, size, fps=30, enduration=2, maxsize=120):
        gap = round((maxsize - size) / 30)
        clip = [
            TextClip(text.encode('utf-8'), fontsize=maxsize - size - x * gap, color='white',
                     font=self.font).set_duration(0.01).set_pos("center").set_start(0.01 * x)
            for x in range(0, fps)
        ]
        clip.append(
            TextClip(text.encode('utf-8'), fontsize=size, color='white', font=self.font).set_pos(
                "center").set_start(clip[-1].end).set_duration(enduration - clip[-1].end))
        return clip

    # text array
    def twinkle(self, text, frame_duration=0.2):
        black = np.zeros([self.screen[1], self.screen[0], 3], dtype=np.uint8)
        black.fill(0)

        white = np.zeros([self.screen[1], self.screen[0], 3], dtype=np.uint8)
        white.fill(255)
        bg = [
            ImageClip(black).set_duration(frame_duration),
            ImageClip(white).set_duration(frame_duration)
        ]

        color = ['white', 'black']

        textarr = [
            TextClip(v.encode('utf-8'), fontsize=20, color=color[i % 2], font=self.font) \
                .set_duration(frame_duration).set_position("center")
            for i, v in enumerate(text)
        ]

        mxingclip = [
            CompositeVideoClip([bg[i % 2], v]) for i, v in enumerate(textarr)
        ]

        return concatenate_videoclips(mxingclip, method='compose')

    def make(self, file_name, save_name):
	logo = VideoFileClip(self.logovideo).resize(height=self.screen[1])
        videos = [ VideoFileClip(f) for f in file_name ]
	videos.append(logo)
        video = concatenate_videoclips(videos, method='compose')
        self.saveVideo(video, save_name)
        return True

    def saveVideo(self, clip, file_name):
        clip.write_videofile(file_name, codec='libx264', threads=4, fps=self.fps)

    # text array
    def step1(self, text, save_name):

        txtClip = TextClip(text[8:9][0].encode('utf-8'), color='white', font=self.font,
                           kerning=5, fontsize=100)
        cvc = CompositeVideoClip([txtClip.set_pos('center')],
                                 size=self.screen)
        letters = findObjects(cvc)

        rotMatrix = lambda a: np.array([[np.cos(a), np.sin(a)],
                                        [-np.sin(a), np.cos(a)]])

        def vortex(screenpos, i, nletters):
            d = lambda t: 1.0 / (0.3 + t ** 8)  # damping
            a = i * np.pi / nletters  # angle of the movement
            v = rotMatrix(a).dot([-1, 0])
            if i % 2: v[1] = -v[1]
            return lambda t: screenpos + 400 * d(t) * rotMatrix(10.5 * d(t) * a).dot(v)

        def cascade(screenpos, i, nletters):
            v = np.array([0, -1])
            d = lambda t: 1 if t < 0 else abs(np.sinc(t) / (1 + t ** 4))
            return lambda t: screenpos + v * 400 * d(t - 0.15 * i)

        def arrive(screenpos, i, nletters):
            v = np.array([-1, 0])
            d = lambda t: max(0, 3 - 3 * t)
            return lambda t: screenpos - 400 * v * d(t - 0.2 * i)

        def vortexout(screenpos, i, nletters):
            d = lambda t: max(0, t)  # damping
            a = i * np.pi / nletters  # angle of the movement
            v = rotMatrix(a).dot([-1, 0])
            if i % 2: v[1] = -v[1]
            return lambda t: screenpos + 400 * d(t - 0.1 * i) * rotMatrix(-0.2 * d(t) * a).dot(v)

        def moveLetters(letters, funcpos):
            return [letter.set_pos(funcpos(letter.screenpos, i, len(letters)))
                    for i, letter in enumerate(letters)]

        clips = [CompositeVideoClip(moveLetters(letters, funcpos),
                                    size=self.screen).subclip(1, 2)
                 for funcpos in [vortex]]

        # WE CONCATENATE EVERYTHING AND WRITE TO A FILE

        final_clip = concatenate_videoclips(clips)

        video = self.twinkle(text[:8], frame_duration=0.4)  # CompositeVideoClip([step1, step1_text_video]).fadein(1)
        video2 = self.twinkle(text[9:12], frame_duration=0.4)  # CompositeVideoClip([step1, step1_text_video]).fadein(1)
        countdown = self.CountDown(text[12:])

        clip = concatenate_videoclips([video, final_clip, video2, countdown], method='compose')
        audio = AudioFileClip(self.step1_audio).subclip(0, clip.end)
        clip.audio = audio
        self.saveVideo(clip, save_name)

        return True

    #
    def step2(self, text, video_name, save_name):
        step2_video = VideoFileClip(video_name).subclip(0, 5)
        step2_video = step2_video.resize(height=self.screen[1])

        step2_text_video = TextClip(text.encode('utf-8'), fontsize=20, color='white',
                                    font=self.font) \
            .set_duration(step2_video.duration).set_pos(lambda t: ('center', 25))

        # clip.set_pos(lambda t: ('center', 50 + t))
        background = ColorClip(size=(720, 72), color=[222, 221, 219], duration=step2_video.duration) \

        background = background.set_opacity(0.4)


        step2_video = CompositeVideoClip([step2_video, background, step2_text_video]).fadein(1).fadeout(1)


        self.saveVideo(step2_video, save_name)

        return True

    def step3(self, text, image_name, save_name):
        white = np.zeros([self.screen[1], self.screen[0], 1], dtype=np.uint8)
        white.fill(255)
        white = ImageClip(white).set_duration(self.step3_duration)
        img = ImageClip(image_name).set_duration(self.step3_duration).resize(0.5).set_pos((150,'center'))
        step3_text_video = TextClip(text.encode('utf-8'), fontsize=100, color='black', size=self.screen,
                                    font=self.font) \
            .set_duration(self.step3_duration).set_pos((100, 'center'))

        clip= CompositeVideoClip([white,img, step3_text_video])
        self.saveVideo(clip, save_name)

    def step4(self, text, video_name, save_name):
        step4_video = VideoFileClip(video_name)
        step4_video = step4_video.resize(height=self.screen[1])
        step4_video.audio = step4_video.audio.subclip(0,2.838)
        audio = AudioFileClip(self.step4_audio).subclip(2, step4_video.end-2.838+2);
        step4_video.audio = concatenate_audioclips([step4_video.audio, audio])
        step4_text_video = TextClip(text.encode('utf-8'), fontsize=20, color='white',
                                    font=self.font) \
            .set_duration(step4_video.duration).set_pos(('center', 'bottom'))

        step4_video = CompositeVideoClip([step4_video, step4_text_video]).fadein(1).fadeout(1)


        self.saveVideo(step4_video, save_name)

        return True

    def step5(self, text, images, save_name):
        blackimage = np.zeros([self.screen[1], self.screen[0], 3], dtype=np.uint8)
        blackimage.fill(0)
        gap = self.step5_duration / len(images)
        step5_video = ImageClip(blackimage).set_duration(self.step5_duration)
        clip_images = [
            ImageClip(x).set_duration(gap).set_position('center').set_start(i * gap).resize(height=self.screen[1])
            for i,x in enumerate(images)
        ]
	step5_text_videos = [
		TextClip(t.encode('utf-8'), fontsize=25, color='white', font=self.font).set_duration(gap).set_position(("center","bottom")).set_start(i * gap) for i,t in enumerate(text)	
	]
        #step5_text_video = TextClip(text.encode('utf-8'), fontsize=20, color='white',
        #                            font=self.font) \
        #    .set_duration(3).set_position(("center","botton"))



        step5_video = CompositeVideoClip([step5_video] + clip_images+ step5_text_videos).fadein(1)

        step5_video.mask.get_frame = lambda t: circle(screensize=(step5_video.w, step5_video.h),
                                               center=(step5_video.w / 2, step5_video.h / 4),
                                               radius=max(0, int(500 - 50 * (t+2) * 2)),
                                               col1=1, col2=0, blur=4)

        self.saveVideo(step5_video, save_name)

        return True

