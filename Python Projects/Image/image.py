from PIL import Image, ImageDraw, ImageFont
 
img = Image.open('Wallpaper.png')
 
fnt = ImageFont.truetype('C:\Windows\Fonts\Bahnschrift.ttf',125)
d = ImageDraw.Draw(img)
txt = input("Name of Guest: ")
d.text((500,470), txt, font=fnt, fill=(0, 0, 0))
 
img.save('Exported-'+txt+'.png')

print("Success!")
