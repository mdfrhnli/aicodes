# pip install opencv-python
import cv2

# use OpenCV's frontal face cascade (comes with opencv package)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('path_to_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
cv2.imwrite('faces_detected.jpg', img)
print(f"Detected {len(faces)} faces.")
