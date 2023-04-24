# By Amir Gheshlaghi

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
t0 = time.time()

while True:
	ret, frame = cap.read()

	if ret:

		t1 = time.time() - t0
		t1_str = str(round(t1, 2))

		# Normal image
		frame1 = cv2.flip(frame, 1)

		# Red image	
		frame2 = frame1.copy()
		frame2[:, :, 2] = 255	

		# Inv image	
		frame3 = 255-frame1

		# Gray image	
		gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY) 
		frame4 = cv2.merge((gray, gray, gray))

		# Resization	
		frame1r=cv2.resize(frame1, (400, 320))

		# Resization
		frame2r=cv2.resize(frame2, (400, 320))

		# Resization
		frame3r=cv2.resize(frame3, (400, 320))

		# Resization
		frame4r=cv2.resize(frame4, (400, 320))

		# Convert four images into one images		
		frame12 = np.concatenate([frame1r, frame2r], 1)

		frame34 = np.concatenate([frame3r, frame4r], 1)

		frame_tot = np.concatenate([frame12, frame34], 0)

		cv2.putText(frame_tot, t1_str, (358, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
		cv2.putText(frame_tot, "Amir", (364, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

		cv2.imshow("webcam", frame_tot)

		q = cv2.waitKey(1)

		if q == ord('q'):
			break

cv2.destroyAllWindows()
cap.release()