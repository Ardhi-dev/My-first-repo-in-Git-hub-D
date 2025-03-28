from PIL import image
from PIL import ImageFilter
#for bonus task
from PIL import imageEnhance 

with image.open('original.jpg') as pic_original:
    print('image is open/nSize:', pic_original.size)
    print('Format:', pic_original.format)
    print('Type:', pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print('Image is created\nSize:', pic_gray.size)
    print('Format:', pic_gray.format)
    print('Type:', pic_gray.mode)
    pic_gray.show()


    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blurred.jpg')
    pic_blured.show()

    pic_up = pic_original.traspose(Image.ROTATE_180)
    pic_up.save('UP.jpg')
    pic_up.show()

    pic_mirrow = pic_original.transpose(Image.FLIF_LEFT_RIGHT)
    pic_mirrow.save('mirrow.jpg')
    pic_mirrow.show()

    pic_contrast = imageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contrast.jpg')
    pic_contrast.show()

