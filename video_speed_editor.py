import cv2

# choose th desired FPS (frames per second) for the output video
output_fps = 1000

cap = cv2.VideoCapture('input_video.mp4')
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*"MP4V"), output_fps, (500,500) )  # the frame size should match that of input video

# Check if input video is opened
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# read the input video frame by frame and write to the output video
while cap.isOpened() :
    ret, frame = cap.read()

    if ret == True :
        out.write(frame)

    else :
       print('Done')
       break
      
# finishing up
cap.release()
out.release()

cv2.destroyAllWindows()
