#!/usr/bin/python3
import sys
import pygame
from moviepy.editor import VideoFileClip
import cv2


class GameSettings:

	def __init__(self, screen):
		self.settings_selected = True

	def run(self):
		cap = cv2.VideoCapture('resources//videos//tuto.mp4')

		while(cap.isOpened()):
			keyCode = cv2.waitKey(50)
			ret, frame = cap.read()
			frametime = 1

			if ret == False:
				break

			frame = cv2.resize(frame, (1250, 700)) 
			cv2.imshow('Tutoriel',frame)
			cv2.moveWindow('Tutoriel', 95,-32)

			if cv2.getWindowProperty('Tutoriel', 0) < 0:
				break

			if cv2.waitKey(frametime) & 0xFF == ord('q'):
				break
		
		#0xFF

		cap.release()
		cv2.destroyAllWindows() 

		
