#I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard drive and then forgetting about these folders. 
#It would be nice to write a program that could scan the entire hard drive and find these leftover “photo folders.”
#Write a program that goes through every folder on your hard drive and finds potential photo folders. 
#Of course, first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s any folder where more than half of the files are photos. 
#And how do you define what files are photos? First, a photo file must have the file extension .png or .jpg. Also, photos are large images; a photo file’s width and height must both be larger than 500 pixels. This is a safe bet, since most digital camera photos are several thousand pixels in width and height.
from PIL import Image
import os
numPhotoFiles = 0
numNonPhotoFiles = 0
for foldername, subfolders, filenames in os.walk('D:\\git-one'):
    for filename in filenames:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            poza = Image.open(filename)
            width, height = poza.size
            if width > 500 and height > 500:
                numPhotoFiles += 1
            else:
                numNonPhotoFiles += 1
        if not (filename.endswith(".png") or filename.endswith(".jpg")):
            numNonPhotoFiles += 1  
fisiere = numNonPhotoFiles + numPhotoFiles
if numPhotoFiles < int(fisiere/2):
    print(os.path.abspath(foldername))
else:
    print('Number of nonPhoto:' + str(numNonPhotoFiles))
    print('Number of Photo:' + str(numPhotoFiles))
exit(0)