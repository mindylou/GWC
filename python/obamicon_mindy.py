'''
Obamicon Project
Girls Who Code SIP 2016
AOL DC

Summary: 

Get the intensity of each pixel by adding the red, green and blue values.
If the pixel has low intensity (<182) color it  dark blue.
If the pixel is medium/low intensity (between 182 and 364) color it red.
If the pixel is medium/high intensity (between 364 and 546) color it light blue.
If the pixel is high intensity (>546) color it yellow.
The RGB codes for the colors are as follows:
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

Additional documentation can be found here: http://effbot.org/imagingbook/image.htm
'''

#Import Pillow Image Library
from PIL import Image

#Set global constants for colors used in Obamicon
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

#Open the image that you want to Obamicize
im = Image.open("obama.jpg")

def obamicize(image_data):
    '''
    Returns: a new list of image data.
    
    This function creates a new list of pixels that converts an image's pixels into an Obama campaign-style photo.
    
    If the pixel has low intensity (<182) the new pixel will be dark blue.
    If the pixel is medium/low intensity (between 182 and 364) the new pixel will be red.
    If the pixel is medium/high intensity (between 364 and 546) the new pixel will be light blue.
    If the pixel is high intensity (>546) the new pixel will be yellow.
    
    Parameter image_data: a list of pixels 

    '''
    
    #Create a new list 
    newImage = []
    
    #Loop through each pixel in the given list of image data
    for pixel in image_data:
        
        #Retrieve R, G, B values
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        
        #Add RGB values to find intensity
        intensity = red + green + blue
        
        #Using given image intensity values, append the corresponding color tuple to the new list
        if intensity < 182:
            newImage.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newImage.append(red)
        elif intensity >= 364 and intensity < 546:
            newImage.append(lightBlue)
        else:
            newImage.append(yellow)
            
    #Return the new list of pixels
    return newImage

#Retrieve image data of the given image as a list
imDataList = list(im.getdata())

#Obamicize the given image data
obamicized_data = obamicize(imDataList)

#Create a new image with the same mode and size as the given image
obamicized_image = Image.new(im.mode, im.size)

#Copy the pixel values of the obamicized data into the new image
obamicized_image.putdata(obamicized_data)

#Display the image onscreen
obamicized_image.show()
