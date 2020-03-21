#The resizeAndAddLogo.py program in this chapter works with PNG and JPEG files, but Pillow supports many more formats than just these two. 
# Extend resizeAndAddLogo.py to process GIF and BMP images as well.
#Another small issue is that the program modifies PNG and JPEG files only if their file extensions are set in lowercase. 
# For example, it will process zophie.png but not zophie.PNG. Change the code so that the file extension check is case insensitive.
#Finally, the logo added to the bottom-right corner is meant to be just a small mark, but if the image is about the same size as the logo itself, the result will look like Figure 19-16. 
# Modify resizeAndAddLogo.py so that the image must be at least twice the width and height of the logo image before the logo is pasted. Otherwise, it should skip adding the logo.
from PIL import Image
import os
for filename in os.listdir('.'):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        catIm = Image.open(filename)
        catlogo = Image.open('catlogo.png')
        widthL, heigtL = catlogo.size
        width, height = catIm.size
        if width >= 2*widthL and height >= 2*heigtL:
            catIm.paste(catlogo, (width-widthL, height-heigtL))
            catIm.save(filename + 'Logo.png')
        else:
            print('Resizing %s...' % (filename))
            catlogo = catlogo.resize((int(width/2), int(height/2)))
            catIm.paste(catlogo, (width-int(width/2), height-int(height/2)),catlogo)
            catIm.save(filename + 'Logo.png')
exit(0)              
