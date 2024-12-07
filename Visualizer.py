import PIL.Image
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk

#create the GUI
#Vizualize the pixelLists given from main
class Visualizer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI2 Visualizer")
        self.root.geometry('409x817+100+100')


    def VisualizePixels(self, pixelList):
        self.pixelList = pixelList
        self.img1 = ImageTk.PhotoImage(pixelList[0])
        self.img2 = ImageTk.PhotoImage(pixelList[1])
        self.img3 = ImageTk.PhotoImage(pixelList[2])
        self.img4 = ImageTk.PhotoImage(pixelList[3])
        self.img5 = ImageTk.PhotoImage(pixelList[4])
        self.img6 = ImageTk.PhotoImage(pixelList[5])
        self.img7 = ImageTk.PhotoImage(pixelList[6])
        self.img8 = ImageTk.PhotoImage(pixelList[7])
        self.img1Holder = tk.Label(self.root, image=self.img1)
        self.img2Holder = tk.Label(self.root, image=self.img2)
        self.img3Holder = tk.Label(self.root, image=self.img3)
        self.img4Holder = tk.Label(self.root, image=self.img4)
        self.img5Holder = tk.Label(self.root, image=self.img5)
        self.img6Holder = tk.Label(self.root, image=self.img6)
        self.img7Holder = tk.Label(self.root, image=self.img7)
        self.img8Holder = tk.Label(self.root, image=self.img8)
        self.img1Holder.grid(row=0, column=0)
        self.img2Holder.grid(row=0, column=1)
        self.img3Holder.grid(row=1, column=0)
        self.img4Holder.grid(row=1, column=1)
        self.img5Holder.grid(row=2, column=0)
        self.img6Holder.grid(row=2, column=1)
        self.img7Holder.grid(row=3, column=0)
        self.img8Holder.grid(row=3, column=1)
        self.root.update()




