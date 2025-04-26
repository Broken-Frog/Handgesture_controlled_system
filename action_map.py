import pyautogui
import time


def right_arrow():
    print("Gesture: Open Palm → Right Arrow")
    pyautogui.keyDown('right')
    time.sleep(0.15)
    pyautogui.keyUp('right')
    

    

def left_arrow():
    print("Gesture: Fist → Left Arrow")
    pyautogui.keyDown('left')
    time.sleep(0.15)
    pyautogui.keyUp('left')

def close_tab():
    print("Gesture: Gun Right → Close Window")
    pyautogui.hotkey('alt', 'f4')

def minimize_window():
    print("Gesture: ✌️ → Minimize Window")
    pyautogui.hotkey('win', 'down')

def recent_tabs():
    print("Gesture: 👈 → Switch to Recent Tabs")
    pyautogui.hotkey('ctrl', 'shift', 'tab') 

def recent_window():
    print("Thumb + Index touching ")
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.keyUp('alt')


def enter():
    print("Gesture:👍 Enter")
    pyautogui.press('enter')

def space_key():
    pyautogui.press('space')
    print("space")
def scroll_down():
    pyautogui.scroll(-500)
    print("Scroll down")
