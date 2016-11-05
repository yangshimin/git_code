from PIL import Image, ImageDraw, ImageFont

sourceFileName = "c:/users/mu yi yang/desktop/psbe.jpg"
avatar = Image.open(sourceFileName)
drawAvatar = ImageDraw.Draw(avatar)

xSize, ySize = avatar.size
fontsize = min(xSize,ySize) // 11
myFont = ImageFont.truetype('c:/Windows/Fonts/Arial.ttf',fontsize)

#drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
    #fill = (255, 100, 0), width = 3)
#drawAvatar.line([0, 0.67 * ySize, xSize, 0.67 * ySize],\
    #fill = (255, 0, 0), width = 3)
#drawAvatar.arc([0, 0, xSize, ySize], 0, 90,\
    #fill = (255, 100, 255))
#drawAvatar.text([0.9 * xSize, 0.1 * ySize - drawAvatar.textsize('3')[1]],\
	#"3",fill = (128, 0, 128))
drawAvatar.text([0.9 * xSize, 0.1 * ySize - fontsize],\
    "3", fill = (255, 0, 0), font = myFont)

del drawAvatar

avatar.save('New_psbe.jpg')
avatar.show()