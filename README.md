# gif-to-cv2-
convert gif to cv2 compatible frames 


##installation 
``` pip install -r requirements.txt``` 

## usage :
```from gifop import *


mk=ungif("picture.gif")
#converts gif to frames 
# returns frameslist (a list of string of path containing all frames)
Invert_gifcolor("picture.gif")
# inverts color of gif turns positive to negative 
pack_gif(mk,"normal")
#packs all frames to a gif with name normal
# mk is list of path of frames 
