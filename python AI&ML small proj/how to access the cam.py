# importing our requirements
import cv2
# using extension for video camera
vid = cv2.VideoCapture(0)
while(True):
 	# taking a camera outline
	# by frame
	ret, frame = vid.read()
    # Displaying our output frame
	cv2.imshow('frame', frame)
	#applying quit key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()