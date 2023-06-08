import pyautogui, cv2, numpy

size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
file_name = input().strip().replace(' ', '_') + '.avi'
fps = 30

video = cv2.VideoWriter(file_name, fourcc, fps, (size))

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    numpy_array = numpy.array(img)
    img_final = cv2.cvtColor(numpy_array, cv2.COLOR_BGR2RGB)

    video.write(img_final)
    cv2.imshow('Live', img_final)

    if cv2.waitKey(1) == 32:
       cv2.waitKey(0)
    elif cv2.waitKey(1) == ord('q'):
      break

cv2.destroyAllWindows()
video.release()






