from PIL import ImageFilter
from PIL import Image

im=Image.open("gorila.jpg")
im=im.convert("RGB")
blurred_image=image.filter(ImageFilter.BLUR)
blurred_image.show()
