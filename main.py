import pyautogui, cv2, numpy, datetime
from datetime import datetime


# width, height = pyautogui.size()
size = (1280, 768)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

file_name = input() + '.avi'
fps = 20

video = cv2.VideoWriter(file_name, fourcc, fps, (size))

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

def pause():
   cv2.waitKey(0)

while True:
    img = pyautogui.screenshot()
    numpy_array = numpy.array(img)
    img_final = cv2.cvtColor(numpy_array, cv2.COLOR_BGR2RGB)

    video.write(img_final)
    #  cv2.imshow('recold', img_final)
    cv2.imshow('Live', img_final)

    if cv2.waitKey(1) == 32:
      pause()
    elif cv2.waitKey(1) == ord('q'):
      break


cv2.destroyAllWindows()
video.release()









