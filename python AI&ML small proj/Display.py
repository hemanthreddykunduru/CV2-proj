import cv2
import numpy as np
from PIL import ImageGrab

while True:
    # Capture the screen
    screen = np.array(ImageGrab.grab())
    
    # Convert the screen to RGB
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)
    
    # Display the screen
    cv2.imshow('Display', screen)
    
    # Wait for a key press and check if it's 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()
