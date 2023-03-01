import cv2 as cv


def ReadImage():
    #Image capture path
    imgPath = 'Photos/cat.jpg'

    img = cv.imread(imgPath)

    cv.imshow('Cat', img)

def ReadVideo():
    vidPath = ''

    # Video capture requires existing path on computer or integer representing camera connection[?]
    ###
    # 0 - Laptop webcam
    # 1 - Connected USB webcam?
    ###

    # Specify input video
    capture = cv.VideoCapture(0)


    while True:
        # Read each frame of the video
        isTrue, frame = capture.read()

        #Show each fram of video in a window
        cv.imshow('Video', frame)

        #Stop reading if 'D' key is pressed
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

ReadVideo()

#Waits for delay in milliseconds for key to be pressed
cv.waitKey(0)
