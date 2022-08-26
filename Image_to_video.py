from moviepy.editor import *

img = ['01.png', '02.png', '03.png', '04.png']

clips = [ImageClip(m).set_duration(2)
      for m in img]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=24)