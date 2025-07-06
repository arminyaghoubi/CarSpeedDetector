from config import VIDEO_PATH
from core.video_reader import VideoReader
import cv2

def main():
    reader=VideoReader(VIDEO_PATH)

    while True:
        frame=reader.read_frame()
        if frame is None:
            break

        cv2.imshow("Video Feed",frame)

        if cv2.waitKey(30) == ord('q'):
            break

    reader.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()