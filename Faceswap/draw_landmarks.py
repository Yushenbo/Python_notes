#-*- coding:utf-8 -*-
#########################################################################
# File Name: draw_landmarks.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

import cv2
import dlib

#loading face detector
detector = dlib.get_frontal_face_detector()
#loading training mode * gain the facial charactor extractor
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#reading image in RGB mode
im = cv2.imread('hc.jpg', cv2.IMREAD_COLOR)

#using detetor to find human face
rects = detector(im, 1)

#Using charactor extractor gai the facial characters
l = [(p.x, p.y) for p in predictor(im, rects[0]).parts()]

#Traverse facial characters & draw
for (cnt, p) in enumerate(l):
    cv2.circle(im, p, 5, (0, 255, 255), 2)
    cv2.putText(im, str(cnt), (p[0] + 5, p[1] - 5), 0, 0.75,
            color=(0, 0, 255))

#save image
cv2.imwrite('landmarks.jpg', im)
cv2.waitKey(0)
