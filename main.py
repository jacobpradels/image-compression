from PIL import Image

def compressImg(img):
    foo = Image.open("sunflower.jpg")
    print(foo.size)
    print(foo.size[0])
    print(foo.size[1])
    foo = foo.resize((int(foo.size[0]/10),int(foo.size[1]/10)),Image.ANTIALIAS)
    foo.save("image_scaled.jpg",quality=95)