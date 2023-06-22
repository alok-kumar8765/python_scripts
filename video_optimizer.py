# Video Optimizer
# pip install moviepy
import moviepy.editor as pyedit
# Load the Video
video = pyedit.VideoFileClip("vid.mp4")
# Trimming
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
final_vid.write_videofile("subclip.mp4")
# Speed up the video
final_vid = final_vid.speedx(2)
final_vid.write_videofile("seepdup.mp4")
# Adding Audio to the video
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)
final_vid.write_videofile("audio.mp4")
# Reverse the Video
final_vid = final_vid.fx(pyedit.vfx.time_mirror)
final_vid.write_videofile("reverse.mp4")
# Merge two videos
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
final_vid.write_videofile("merge.mp4")
# Add VFX to Video
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
final_vid.write_videofile("vfx.mp4")
# Add Images to Video
img1 = pyedit.ImageClip("Image1.jpeg")
img2 = pyedit.ImageClip("Image2.jpeg")
final_vid = pyedit.concatenate_videoclips([img1, img2])
# Save the video
final_vid.write_videofile("img.mp4")
