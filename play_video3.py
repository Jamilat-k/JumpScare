from gpiozero import MotionSensor
from picamera import PiCamera
import cv2

# Load video
video_path = '/home/pi/Desktop/video.mp4'
cap = cv2.VideoCapture(video_path)

# Read the first frame
ret, frame = cap.read()

# Display the first frame
cv2.imshow('Video Playback', frame)

# Initialize motion sensor
motion_sensor = MotionSensor(pin=4)
motion_detected = False

# Load still image
still_image_path = '/home/pi/Desktop/still.png'
still_image = cv2.imread(still_image_path)

while True:
    # Check if motion is detected
    if motion_sensor.motion_detected:
        motion_detected = True
        # Read the next frame
        ret, frame = cap.read()
        cv2.imshow('Video Playback', frame)
    elif motion_detected:
        # Display still image when motion is not detected
        cv2.imshow('Video Playback', still_image)

    # Break the loop if the 's' key is pressed
    if cv2.waitKey(1) == ord('s'):
        break

    # Check if 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Pause the video
        cv2.waitKey(-1)

    # Check if the video has reached the end
    if not ret:
        # Display still image at the end of the video
        cv2.imshow('Video Playback', still_image)
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
