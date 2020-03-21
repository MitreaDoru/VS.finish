#Chapter 15 included a practice project to create custom invitations from a list of guests in a plaintext file. 
#As an additional project, use the pillow module to create images for custom seating cards for your guests. 
#For each of the guests listed in the guests.txt file from the resources at https://nostarch.com/automatestuff2/, generate an image file with the guest name and some flowery decoration. A public domain flower image is also available in the book's resources.
from PIL import Image, ImageDraw, ImageFont
import docx, os
guests = open('guests.txt')
background = Image.open('Flower.png')
for guest in guests:
    guest = guest.rstrip()
    new_image = Image.new('RGBA', (360, 288), 'white')
    new_image.paste(im=background)
    draw = ImageDraw.Draw(new_image)
    draw.rectangle((0, 0, 360, 288), outline='black')
        # get font
    fonts_folder = 'C:\Windows\Fonts'
    arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'arial.ttf'), 36)
        # get font size for center justification
    w, h = draw.textsize(guest, arial_font)
        # draw text of guest name
    draw.text(((300-w)/2, (248-h)/2), guest, fill='grey', font=arial_font)
        # save new image
    new_image.save(guest + 'seating_card.png')
exit(0)