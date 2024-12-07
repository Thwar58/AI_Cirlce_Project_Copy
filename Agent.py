import math
import random

import PIL.Image
from PIL import Image
import numpy as numpy
class Agent:
# hold the fitness function
# process the pixelLists with the fitness function
# give main the new pixelLists

    def __init__(self):
        print("test")
        self.currentScore = -1000000
        
    #gets the fitness of an image
    # with 10 radii, it takes about 1 hour and 20 minutes to hit the goal, a circle can be clearly seen around 40-50 minutes
    def getFitnessValue(self, pixImg):
        #200x200, define center x and y
        x_cent = 100
        y_cent = 100
        maximum = -1000000000

        radii = [20,27,34,41,48,55,62,69,76,83]
        for r in radii:
            in_r = 0
            not_in_r = 0
            for x in range(200):
                for y in range(200):
                    dist = math.dist((y, x), (y_cent, x_cent))

                    isNonWhite = sum(pixImg.getpixel((x,y))) < 255*3
                    if(isNonWhite):
                        if abs(dist - r) <= 5:
                            in_r += 1
                        else:
                            not_in_r += 1
            value = (in_r - not_in_r)
            if value > maximum:
                maximum = value
        #return percentage of fitness
        rtrn = maximum / 40000
        self.currentScore = rtrn
        return rtrn



    #takes an array of 8 images, and eliminates the 4 least fit
    #returns the a list of the 4 most fit images, sorted by fitness
    def cullArray(self, pixelImgArray):
        return_Array = sorted(pixelImgArray, key = lambda x: self.getFitnessValue(x))
        return_Array = return_Array[4:]
        return return_Array


    #breedPair will be called on 4 parents to produce 4 children
    #breedPair takes four pixel images and returns 8 pixel images
    #
    def breedPairs(self, parentPixArray):
        P1 = numpy.array(parentPixArray[3])
        P2 = numpy.array(parentPixArray[2])
        P3 = numpy.array(parentPixArray[1])
        P4 = numpy.array(parentPixArray[0])
        

        pair1Slice = 100
        pair2slice = 100
        # slice the first pair
        P1A = P1[:pair1Slice]
        P1B = P1[pair1Slice:]
        P2A = P2[pair1Slice:]
        P2B = P2[:pair1Slice]

        #combine them into two new arrays
        childA = numpy.concatenate((P1A, P2A))
        childB = numpy.concatenate((P2B, P1B))

        #slice the second pair
        P3A = P3[:pair2slice]
        P3B = P3[pair2slice:]
        P4A = P4[pair2slice:]
        P4B = P4[:pair2slice]

        #combine them into two new arrays
        childC = numpy.concatenate((P3A, P4A))
        childD = numpy.concatenate((P4B, P3B))


        #convert children arrays to img, add to array and return
        newImgA = Image.fromarray(childA, mode = 'RGB')
        newImgB = Image.fromarray(childB, mode = 'RGB')
        newImgC = Image.fromarray(childC, mode = 'RGB')
        newImgD = Image.fromarray(childD, mode = 'RGB')
        parentPixArray.append(newImgA)
        parentPixArray.append(newImgB)
        parentPixArray.append(newImgC)
        parentPixArray.append(newImgD)
        return parentPixArray


    #with 10 radii it is about 80 minutes to goal state, the program then ends
    #a circle can be seen around 40-50 minutes with 10 radii
    def isGoal(self, pixellist):
        print("fitness: " + str(self.currentScore))
        if(self.currentScore > -.4):
            return True
        return False


    #each image has a chance of their pixels being selected
    #of the selected, some become white, the others are random RGB values
    def mutate(self, pixelList):
        for i in range(len(pixelList)):
            pixelImg = pixelList[i]
            #Size determines the percentage of random pixels selected
            randomPixels = numpy.random.choice(40000, size = 400, replace = False)
            switch = 0
            for j in randomPixels:
                if numpy.random.rand() < .1:
                    if(switch % 3 != 0):
                        x = j%200
                        y = j//200
                        pixelImg.putpixel((x, y), (255, 255, 255))
                    else:
                        x = j%200
                        y = j//200
                        pixelImg.putpixel((x, y), (numpy.random.randint(250), numpy.random.randint(250), numpy.random.randint(250)))
                    switch = switch + 1
        return pixelList