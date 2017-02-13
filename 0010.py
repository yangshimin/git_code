from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndchar():
    return chr(random.randint(65, 90))


def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('c:/windows/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndcolor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndchar(), fill=rndcolor2(), font=font)

image = image.filter(ImageFilter.BLUR)
image.show()
image.save('code.jpg')
