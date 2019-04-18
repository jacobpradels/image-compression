from PIL import Image
from path import pathtolist
import tkinter


scaleFactor = 1
def compressImg(img,dir):
    foo = Image.open(str(dir) + "\\" + img)
    # print(foo.size,foo.size)
    foo = foo.resize((int(foo.size[0]/scaleFactor),int(foo.size[1]/scaleFactor)),Image.ANTIALIAS)
    foo.save(dir + "\\c-" + img,quality=10)


top = tkinter.Tk()
top.title("Image compression")
top.geometry("500x500")


w = tkinter.Label(top, text="Input the file path in this text box:")
w.pack()

e = tkinter.Entry(top)
e.pack()

def outputit():
    string = e.get()
    dir = str(string)
    path = pathtolist(dir)
    # print(path)
    # print(dir)
    for file in path:
        compressImg(file,dir)
        # print(type(file))
    

b = tkinter.Button(top, text="OK", command=outputit)
b.pack()
tkinter.mainloop()

    
