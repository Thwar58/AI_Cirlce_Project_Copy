import time

from PIL import Image
import numpy as np
from Visualizer import Visualizer as Visualizer
from Agent import Agent as Agent
import tkinter as tk

#Generate the 8 random pixel RGB arrays
#Use methods from Agent for the fitness function and altering the pixelLists
#Use methods from Vizualizer to display the images at timesteps as they get closer to goal

class Driver:

    #Takes a seed to randomly create the 8 200x200 pixel image objects
    #generate_images takes seed and returns a list of 200x200 random pixel images
    def generate_images(seed: int) -> list[Image.Image]:
        image_list = []
        np.random.seed(seed)
        for i in range(8):
            pixel_array = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
            img = Image.fromarray(pixel_array, mode='RGB')
            image_list.append(img)
#         print(image_list)
        return image_list

    pixelList = generate_images(42)
    Visualizer = Visualizer()
    Agent = Agent()
    #Visualizer.loadGUI()
    Visualizer.VisualizePixels(pixelList)
    gens = 0

    while (Agent.isGoal(pixelList) == False):
        for i in range (2):
            pixelList = Agent.cullArray(pixelList)
            pixelList = Agent.breedPairs(pixelList)
            pixelList = Agent.mutate(pixelList)
            gens = gens+1
            print("generation number : " + str(gens))
        Visualizer.VisualizePixels(pixelList)
        