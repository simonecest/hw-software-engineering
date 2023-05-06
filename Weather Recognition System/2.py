# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  :
# @file    :
# @Time    : 2023/4/21 14:52
# @Function:
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

numbs = 0
def panduan(image):
    global numbs
    rgb_im = image.convert('RGB')

    blue_pixel_count = 0
    threshold = 100
    all1 = image.width * image.height

    for x in range(image.width):

        for y in range(image.height):

            r, g, b = rgb_im.getpixel((x, y))

            if b > threshold:

                if b > r + 20:

                    if b > g + 20:

                        blue_pixel_count += 1

    print("The number of blue pixels:", blue_pixel_count)
    print("百分比:", blue_pixel_count / all1)
    numbs = blue_pixel_count / all1

    if blue_pixel_count/all1 >0.5:
        return True

    return False
FilePath = ""

# 创建根窗口
root = tk.Tk()

root.geometry("840x500")

root.title('Weather Recognition System')

w1 = tk.Label(root, text="")
# canvas = tk.Canvas(root, width=600, height=600)
# canvas.create_rectangle(2, 2, 454, 454, outline='blue', width=2)
# canvas.place(x=20, y=20)
canvas = tk.Canvas(root, width=600, height=600)
# canvas.create_image(0, 0, anchor='nw')
canvas.create_rectangle(2, 2, 454, 454, outline='blue', width=2)
canvas.place(x=20, y=20)
tianqis = ""
photo = ""
image_logo = Image.open("logo.jpg")

logos = ImageTk.PhotoImage(image_logo)
# show photo
# canvas = tk.Canvas(root, width=image_file.width, height=image_file.height)
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.create_image(0, 0, anchor='nw', image=logos)
canvas1.place(x=550, y=210)
def getfile():
    global FilePath,tianqis,photo

    FilePath = filedialog.askopenfilename(title=u'Open', filetypes=[("Image", ".jpg")])

    if FilePath:
        # 加载图像
        image_file = Image.open(FilePath)
        w, h = image_file.width, image_file.height
        # print(w,h)
        if image_file.width > image_file.height:
            # print("there")
            w = 450
            h = int(image_file.height / (image_file.width / 450))
        elif image_file.height > image_file.width:
            # print("theres")
            h = 450
            w = int(image_file.width / (image_file.height / 450))

        print("wh",w,h)
        img = image_file.resize((w, h), Image.ANTIALIAS)

        tianqis = panduan(img)
        photo = ImageTk.PhotoImage(img)
        # show photo
        # canvas = tk.Canvas(root, width=image_file.width, height=image_file.height)
        canvas.create_image(3, 3, anchor='nw', image=photo)

        canvas.place(x=20, y=20)
        w1 = tk.Label(root, text="                            ",font=('Helvetica', '20'))
        w1.place(x=650, y=130)
        w2 = tk.Label(root, text="                            ", font=('Helvetica', '20'))
        w2.place(x=650, y=170)

tianqi = ["Sunny","Not Sunny"]

def show():
    if tianqis:
        w1 = tk.Label(root, text=tianqi[0],background="red",font=('Helvetica', '20'))
        w1.place(x=650, y=130)
        w2 = tk.Label(root, text=f"{round(numbs*100,4)}%", background="blue", font=('Helvetica', '20'))
        w2.place(x=650, y=170)

    elif photo:
        w1 = tk.Label(root, text=tianqi[1],background="yellow",font=('Helvetica', '20'))
        w1.place(x=650, y=130)
        w2 = tk.Label(root, text=f"{round(numbs*100,4)}%", background="blue", font=('Helvetica', '20'))
        w2.place(x=650, y=170)

    else:
        w1 = tk.Label(root, text="                            ",font=('Helvetica', '20'))
        w1.place(x=650, y=130)
        w2 = tk.Label(root, text="                            ", font=('Helvetica', '20'))
        w2.place(x=650, y=170)

# 创建两个按钮
button1 = tk.Button(root, text="Open Photo", width=20, height=2,command=getfile)
button1.place(x=650,y=20)

button2 = tk.Button(root, text="Calculate Weather", width=20, height=2,command=show)
button2.place(x=650,y=80)

root.mainloop()