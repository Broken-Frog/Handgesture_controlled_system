import cv2
import mediapipe as mp
import time
import action_map

class GestureHandler:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
        self.drawing = mp.solutions.drawing_utils
        self.last_trigger_time = 0
        self.cooldown = 1  # seconds

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                self.drawing.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                fingers = self.fingers_up(hand)
                self.check_gesture(fingers)

        return frame

    def fingers_up(self, hand_landmarks):
        tips_ids = [4, 8, 12, 16, 20]
        fingers = []

        fingers.append(1 if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x else 0)

        for i in range(1, 5):
            fingers.append(1 if hand_landmarks.landmark[tips_ids[i]].y < hand_landmarks.landmark[tips_ids[i] - 2].y else 0)

        return fingers

    def check_gesture(self, fingers):
        now = time.time()
        if now - self.last_trigger_time < self.cooldown:
            return

        gesture_map = {
            (1, 1, 1, 1, 1): action_map.right_arrow,        
            (0, 0, 0, 0, 0): action_map.left_arrow,         
            (1, 1, 0, 0, 1): action_map.close_tab,          
            (0, 1, 1, 0, 0): action_map.minimize_window,    
            (1, 1, 0, 0, 0): action_map.recent_tabs,
            (0, 0, 1, 1, 1): action_map.recent_window,        
            (1, 0, 0, 0, 0): action_map.enter,
            (0, 0, 0, 0, 1):action_map.space_key,
            (0, 1, 0, 0, 0):action_map.scroll_down
        }


        func = gesture_map.get(tuple(fingers))
        if func:
            func()
            self.last_trigger_time = now

            
            
