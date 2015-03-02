import os
import time
import cv2
import numpy as np
import picamera

#global_vars
cam = None
cam_created = False
working_directory = os.path.dirname(os.path.abspath(__file__))

class cam_controller:
	def __init__(self):
		pass
	
	def create_cam(self):
		global cam_created, cam
		try:
			cam = picamera.PiCamera()
			cam_created = True
			return cam
		except:
			cam_created = False
			return None

	def check_for_cam(self):
		pass

	def start_recording(mode, split_interval, resolution, path, isopencvmode):
		global cam_created
		cam = self.create_cam()
		if isopencvmode == True:
			# Create the in-memory stream
			stream = io.BytesIO()
			with picamera.PiCamera() as camera:
				camera.start_preview()
    			time.sleep(2)
    			camera.capture(stream, format='jpeg')
			# Construct a numpy array from the stream
			data = np.fromstring(stream.getvalue(), dtype=np.uint8)
			# "Decode" the image from the array, preserving colour
			image = cv2.imdecode(data, 1)
			# OpenCV returns an array with data in BGR order. If you want RGB instead
			# use the following...
			image = image[:, :, ::-1]
		else:
			cam_created.resolution = (resolution[0], resolution[1])
    		cam_created.start_recording('1.h264')
    		cam_created.wait_recording(5)
    		for i in range(2, 11):
				cam_created.split_recording('%d.h264' % i)
				cam_created.wait_recording(split_interval)
    		cam_created.stop_recording()


