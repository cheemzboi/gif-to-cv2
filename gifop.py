import imageio
import cv2
import os
from PIL import Image
import numpy as np



def showop():
    return
path = os.getcwd()
# Set then name of your folder
'''Replace this name with what you want your folder name to be'''
folder_name = 'gif_frames'
def Image_Inversion(Image):
	Height = Image.shape[0]
	Width = Image.shape[1]
	Channels = Image.shape[2]
	
	Size = (Height, Width, Channels)
	
	New_Image = np.zeros(Size, np.uint8)
	
	for x in range(0, Height):
		for y in range(0, Width):
			for c in range(0, Channels):
				New_Image[x,y,c] = 255 - Image[x,y,c]
	return New_Image

def ungif(gifpath):
    framelist = []
    '''Output gif as frames saves the frames in a folder and returns a list containing the frames'''
    i = 0
    gif = imageio.mimread(gifpath)
    nums = len(gif)
    path = os.getcwd()
    # Set then name of your folder
    '''Replace this name with what you want your folder name to be'''
    folder_name = 'gif_frames'
    # If the folder does not exist, then make it
    if not os.path.exists(path + '/' + folder_name):
        os.makedirs(path + '/' + folder_name)

    print("Total {} frames in the gif!".format(nums))
    # convert form RGB to BGR 
    imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
    for i in range(nums):
        
        cv2.imwrite(os.path.join(path + '/' + folder_name,"Frames"+str(i+1)+".png"), imgs[i])
        framelist.append(os.path.join(path + '/' + folder_name,"Frames"+str(i+1)+".png"))
    
    return framelist

def pack_gif(frameslist:list,name:str="Packed_Gif"):
    frames = []
    for number in range(len(frameslist)):
        #inkm=os.path.join(path + '/' + folder_name,"Frames"+str(number+1)+".png")
        frames.append(Image.open(frameslist[number]))
        
    frame_one = frames[0]
    name=name+".gif"
    frame_one.save(str(name), format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)
    
def Invert_gifcolor(gifpath):
    i = 0
    mk=ungif(gifpath)
    invlist=[]
    for i in range(0,len(mk)):
        Input_Image = cv2.imread(mk[i])
        Inverted_Image = Image_Inversion(Input_Image)
        cv2.imwrite(os.path.join(path + '/' + folder_name,"invFrames"+str(i+1)+".png"), Inverted_Image)
        invlist.append(os.path.join(path + '/' + folder_name,"invFrames"+str(i+1)+".png"))
    pack_gif(invlist,"Inverted_Gif")
        

    

mk=ungif("picture.gif")
Invert_gifcolor("picture.gif")
pack_gif(mk,"normal")