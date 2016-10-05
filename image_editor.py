from PIL import Image
catIm = Image.open('/home/prakash/Desktop/index.jpeg')
print dir(catIm)
newimg= catIm.resize((256,256))
newimg.save('/home/prakash/Desktop/new_size.png', 'png')

#resize= catIm.rotate(30)
#resize.save('/home/prakash/Desktop/resized.png')

#croppedIm= catIm.crop((3,4,4,6))
#croppedIm.save('cropped.png')