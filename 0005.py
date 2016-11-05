from PIL import Image as img
import os

imgTypes = ['.png','.jpg','.bmp']
fileDir = "E:" + os.sep + "test"

Iphone_Size = (1136,640)

for root , dirs , files in os.walk(fileDir):
	for currentfile in files:
		crtFile = root + "\\" + currentfile
		if crtFile[crtFile.rindex('.'):].lower() in  imgTypes:
			im = img.open(crtFile)
			crtsize = im.size
			if crtsize[0] >= Iphone_Size[0] or crtsize[1] >= Iphone_Size[1]:
				crtsize = Iphone_Size
				im.thumbnail(crtsize)
			else:
				im.thumbnail(crtsize)
			outfile = os.path.join('E:' + os.sep + 'Img_Test', currentfile)
			print (outfile)
			im.save(outfile)
