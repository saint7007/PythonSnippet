# import image module from pillow
from PIL import Image,ImageSequence

# open the image
Image1 = Image.open('/home/amsys/Documents/projects/Airflow_code/Kate-Winslet.jpg')

# make a copy the image so that
# the original image does not get affected
Image1copy = Image1.copy()
Image2 = Image.open('/home/amsys/Documents/projects/Airflow_code/1.png').convert("RGBA")
Image2copy = Image2.copy()
animated_gif = Image.open("/home/amsys/Documents/projects/Airflow_code/tenor2.gif").convert("RGBA")

# paste image giving dimensions
Image1copy.paste(Image2copy, (70, 150))

# save the image
Image1copy.save('pasted2.png')
frames = []
i=0
animated_gif = Image.open("/tenor2.gif")

# for j in range(1,400):
for frame in ImageSequence.Iterator(animated_gif):
    i=i+50
    Image1copy.paste(Image2copy, (70, 150+i))
    frames.append(Image1copy)
frames[0].save('output1.gif', save_all=True, append_images=frames[1:],optimize=False, duration=40, loop=0)



from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
