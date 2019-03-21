from tkinter import *
import cv2
from PIL import Image as im

codeLib = ''' i-a*ov*inc*an'''
count = len(codeLib)


def transform(image_file):
    codePic = ''
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            g, r, b = image_file.getpixel((w, h))
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            codePic = codePic + codeLib[int(((count - 1) * gray) / 256)]
        codePic = codePic + '\r\n'
    return codePic


def image2char(image_file):
    image_file = image_file.resize((int(image_file.size[0] * 0.16), int(image_file.size[1] * 0.06)))  # 调整图片大小
    return transform(image_file), image_file.size[0], image_file.size[1]


def frame2image(cap, i):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    _, b = cap.read()
    image = im.fromarray(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
    return image


def gui(path):
    cap = cv2.VideoCapture(path)
    root = Tk()
    t = frame2image(cap, 0)
    _, w, h = image2char(t)
    text = Text(root, width=w, height=h)
    text.pack()
    framenum = int(cap.get(7))
    for i in range(framenum):
        image = frame2image(cap, i)
        content, _, _ = image2char(image)
        text.insert(INSERT, content)
        root.update()
        text.delete(0.0, END)


if __name__ == '__main__':
    gui(r'pp.mp4')
