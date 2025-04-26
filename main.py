import cv2
from gesture_core import GestureHandler

def main():
    cap = cv2.VideoCapture(0)
    handler = GestureHandler()

    while True:
        success, frame = cap.read()
        if not success:
            continue

        frame = handler.process_frame(frame)

        cv2.imshow("Gesture Keyboard Trigger", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()