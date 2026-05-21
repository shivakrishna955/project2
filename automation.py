import pyautogui
import webbrowser
import os


def open_youtube():
    webbrowser.open("https://youtube.com")


def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")


def open_notepad():
    os.system("notepad")