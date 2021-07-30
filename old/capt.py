from threading import Thread
import imutils
import cv2, time

camlink1 = "rtsp://192.168.0.2:554/h264?username=admin&password=123456"
camlink2 = "rtsp://192.168.0.3:554/h264?username=admin&password=123456"

class VideoStreamWidget(object):
    def __init__(self, link, camname, src=0):
        self.capture = cv2.VideoCapture(link)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        self.camname = camname
        self.link = link
        print(camname)
        print(link)

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def show_frame(self):

        # Display frames in main program
        frame = imutils.resize(self.frame, width=400)
        cv2.imshow('Frame ' + self.camname, frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget(camlink1,"Cam1")
    video_stream_widget2 = VideoStreamWidget(camlink2,"Cam2")

    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget2.show_frame()
        except AttributeError:
            pass