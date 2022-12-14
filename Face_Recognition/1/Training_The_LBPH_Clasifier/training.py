from PIL import Image
import cv2 as cv
import numpy as np
import os

def get_image_data():
    paths = [os.path.join('./Face_Recognition/1/yalefaces',f) 
    for f in os.listdir('./Face_Recognition/1/yalefaces')] #we are perring the file in the format of a list
                                                           #we will get the full path of the image, using the join commands,
                                                           #it will join the first path with the path of the file in that directory
                                                           #that the for loop will traverse
    #print(paths)
    faces = [] #store information about the list ( information about the pixels)
    ids = [] #store the name of the classes, because we have from subject 1 to subject 15, in this example
    for path in paths:
        #print(path)
        image = Image.open(path).convert('L') #we are reading the images with the Image class 
                                              #because the images are stored as gif images
                                              #we have to convert with set the parameter "L" and it means the mode of the image
                                              #if we have an "L" mode images, it means it is a sinlge channel image, which is
                                              #interpreted as a gray scale image, the letter "L" means is just store the
                                              #luminance of the image, it is a compact format, but only stores a gray scale not colors
                                              #in other words we are converting from a clolr image to a gray scale image
        #print(type(image))
        image_np = np.array(image) #"unit8" means each pixel of the image is an integer value (unit8 doesn't work)
        #print(type(image_np))
        id = int(os.path.split(path)[1].split('.')[0].replace('subject','')) #will split when will find a space
        #print(id)
        ids.append(id)
        faces.append(image_np)
        
    return np.array(ids), faces

        
ids,faces = get_image_data()
print(faces[0], faces[0].shape)

lbph_classifier = cv.face.LBPHFaceRecognizer_create() #for this one we have a lot of parameters and I don't understand are grid_x and also grid_y
                                                      # the default value for grid_x and grid_y is 8
lbph_classifier.train(faces, ids) # face variable stores all the pixels of all the images
                                  # ids variable stores all the name of the images of the classes, each number represents a person
                                  # the algorithm will store 64 histogram for each face

lbph_classifier.write('lbpg_classifier.yml') #this files stores each histogram of each one of the images


