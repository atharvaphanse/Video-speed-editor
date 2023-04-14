import cv2
import numpy as np

output_fps = 1000

cap = cv2.VideoCapture('input_video.mp4')
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*"MP4V"), output_fps, (500,500) )

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while cap.isOpened() :
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True :
        out.write(frame)

    else :
       print('Done')
       break
    
# When everything done, release the video capture object
cap.release()
out.release()

cv2.destroyAllWindows()