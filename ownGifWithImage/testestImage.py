from PIL import Image, ImageSequence
import cv2

size = 320, 240

transparent_foreground = Image.open("/Kate-Winslet.jpg").convert("RGBA")
size=transparent_foreground.size
print(size)
animated_gif = Image.open("/Webp.net-resizeimage.gif")

frames = []
for frame in ImageSequence.Iterator(animated_gif):
    frame = frame.copy()
    frame.thumbnail((size[0],size[1]), Image.ANTIALIAS)
    frame.paste(transparent_foreground, mask=transparent_foreground)
    frames.append(frame)
frames[0].save('output.gif', save_all=True, append_images=frames[1:],transparency=0)