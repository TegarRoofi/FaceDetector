import cv2

face_reff = cv2.CascadeClassifier("face_reff.xml")
camera = cv2.VideoCapture(0)

def face_detection(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_reff.detectMultiScale(optimized_frame, scaleFactor=1.1, minSize=(30, 30), minNeighbors=5)
    return faces

def box(frame):
    for x, y, w, h in face_detection(frame):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)

def cloe_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        box(frame)
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cloe_window()

if __name__ == "__main__": 
    main()