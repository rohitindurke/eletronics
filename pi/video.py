import picamera as PiCamera
import time

camera = PiCamera()
camera.resolution = (420,420)
camera.start_recording("path.mp4")
time.sleep(6)
camera.stop_recording()