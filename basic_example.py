import os
import cv2 as cv
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

RTSP_USERNAME = os.getenv("RTSP_USERNAME")
RTSP_PASSWORD = os.getenv("RTSP_PASSWORD")
RTSP_IP = os.getenv("RTSP_IP")
RTSP_PORT = os.getenv("RTSP_PORT")
RTSP_URL = f"rtsp://{RTSP_USERNAME}:{RTSP_PASSWORD}@{RTSP_IP}:{RTSP_PORT}/onvif1"

capture = cv.VideoCapture(RTSP_URL, cv.CAP_FFMPEG)

while True:
    result, frame = capture.read()
    if result:
        cv.imshow("Video", frame)
        if cv.waitKey(1) == ord("q"):
            break
    else:
        print("Unable to connect")
        break

capture.release()
