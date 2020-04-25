from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))

draw = ImageDraw.Draw(img)
draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

img.save('test.gif', 'GIF', transparency=0)