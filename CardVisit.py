import os
from PIL import Image, ImageFont, ImageDraw # pip install Pillow
import qrcode # pip install qrcode

# input user's name
myname = input("Enter your name: ")
# read background file
mycard = Image.open("background.png")
# read word font
myfont = ImageFont.truetype("ZenAntiqueSoft-Regular.ttf", 100) # download on google font
# make qr code
img = qrcode.make(str(myname))
img.save(str(myname) + '.bmp')

# read the qrcode file
im = Image.open(str(myname) + '.bmp')
# Copy the qrcode to the card
mycard.paste(im, (15, 15)); os.remove(str(myname) + '.bmp')
# Insert user's name to the card
image_editable = ImageDraw.Draw(mycard) 
image_editable.text((15,450), myname, (237, 230, 211), font = myfont) 

mycard.save(myname + '.png')