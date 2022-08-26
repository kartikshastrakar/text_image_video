from PIL import Image, ImageDraw, ImageFont
import os

def text_on_img(filename='04.png', text="Hello", size=12):
	"Draw a text on an Image, saves it, show it"
	fnt = ImageFont.truetype('arial.ttf', size)
	# create image
	image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = "red")
	draw = ImageDraw.Draw(image)
	# draw text
	draw.text((10,10), text, font=fnt, fill=(255,255,0))
	# save file
	image.save(filename)
	# show file
	os.system(filename)


text_on_img(text="And i fun loving person and animal lover ", size=300)