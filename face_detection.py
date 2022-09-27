import cv2 
import os 
haar = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(img, draw_box=True):
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = haar.detectMultiScale(grayscale_img, scaleFactor=1.6)
    
    # draw bounding box 
    for(x,y, width, height) in faces:
        if draw_box: 
            cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0),5) # draw a bounding box starting at x,y with color red
    face_box = img[y:y+height, x:x+width]
    face_coords = [x,y, width, height]
    return img, face_box, face_coords


# test detection 
def detect_faces_test():
    faces = os.listdir('faces')
    print(faces)
    images = [face for face in faces if 'jpg' in face]# create a list of faces if the file type is jpg

    for image in images: 
        img = cv2.imread('faces/' + image)
        detected_face, _ , _ = detect_faces(img)
        cv2.imwrite('faces/detected/' + image, detected_face)

detect_faces_test()