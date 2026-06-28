from time import strftime, sleep
from pyautogui import screenshot
from os.path import join
def take_screenshot(screenshot_dir):
    timestamp=strftime("%Y-%m-%d_%H-%M-%S")
    filename=join(screenshot_dir,f"screenshot_{timestamp}.png")
    #"C:\Users\HP\Desktop\Yeni klasör (2)"_2026-03-30_05-05.png
    #"C:\Users\HP\Desktop\Yeni klasör (2)"_2026-03-30_05-10.png
    img=screenshot()
    img.save(filename)
    print(f"ekran goruntusu alindi: {filename}")

file_path = r"C:\Users\HP\Desktop\Yeni klasör (2)"

while True:
    take_screenshot(file_path)
    sleep(5)
